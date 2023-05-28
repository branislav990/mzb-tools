import csv
import io

from django.shortcuts import render, redirect
from .forms import *
from django.views import View
from index_calculator.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages


class IndexCalculator(View):

    def get(self, request):
        bmwp = request.session.get('bmwp', False)
        whpt = request.session.get('whpt', False)
        cci = request.session.get('cci', False)
        lifesp = request.session.get('lifesp', False)
        lifef = request.session.get('lifef', False)
        psis = request.session.get('psis', False)
        psif = request.session.get('psif', False)
        dehli = request.session.get('dehli', False)
        epsir = request.session.get('epsir', False)
        epsip = request.session.get('epsip', False)
        ukbap = request.session.get('ukbap', False)
        site_date = request.session.get('site_date', False)

        if bmwp:
            del (request.session['bmwp'])
        if whpt:
            del (request.session['whpt'])
        if cci:
            del (request.session['cci'])
        if lifesp:
            del (request.session['lifesp'])
        if lifef:
            del (request.session['lifef'])
        if psis:
            del (request.session['psis'])
        if psif:
            del (request.session['psif'])
        if dehli:
            del (request.session['dehli'])
        if epsir:
            del (request.session['epsir'])
        if epsip:
            del (request.session['epsip'])
        if ukbap:
            del (request.session['ukbap'])
        if site_date:
            del (request.session['site_date'])

        form_csv = UploadFileForm()
        form_dehli = UploadDehliForm()
        context = {
            'form_csv': form_csv,
            'form_dehli': form_dehli,
            'site_date': site_date,

            'bmwp': bmwp,
            'whpt': whpt,
            'cci': cci,
            'lifesp': lifesp,
            'lifef': lifef,
            'psis': psis,
            'psif': psif,
            'dehli': dehli,
            'epsir': epsir,
            'epsip': epsip,
            'ukbap': ukbap,
        }

        return render(request, 'base.html', context)


    def post(self, request):
        form_csv = UploadFileForm(request.POST, request.FILES)
        form_dehli = UploadDehliForm(request.POST, request.FILES)
        if form_csv.is_valid() and form_dehli.is_valid():

            file_csv = request.FILES['csv_file']
            if not file_csv.name.endswith('.csv'):
                messages.error(request, 'File must be of CSV type')
                return redirect('index_calculator')
            try:
                data_set_csv = file_csv.read().decode('UTF-8')
                io_string_csv = io.StringIO(data_set_csv)
            except UnicodeDecodeError:
                messages.error(request, 'The CSV file is not in the correct format')
                return redirect('index_calculator')

            try:
                file_dehli = request.FILES['dehli_file']
                if not file_dehli.name.endswith('.csv'):
                    messages.error(request, 'File must be of CSV type')
                    return redirect('index_calculator')
                data_set_dehli = file_dehli.read().decode('UTF-8')
                io_string_dehli =io.StringIO(data_set_dehli)
            except:
                pass


            def bmwp_aspt(csv_file):
                """Calculation of BMWP score and ASPT"""
                n_taxa = 0
                bmwp_score = 0
                families = []
                taxons = []
                ancylidae = ['ancylus fluviatilis', 'ancylus sp.', 'ancylidae',
                             'ancylidae/acroloxidae', '"ancylidae" gen. sp.']
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon'])
                        taxons.append(taxon)
                    # except (ObjectDoesNotExist, TypeError):
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    # Ancylidae used to be a separate family, now they belong
                    # to Planorbide, but their BMWP score values differ
                    if row['taxon'].lower() in ancylidae:
                        if 'ancylidae' in families:
                            pass
                        else:
                            bmwp_score += 6
                            n_taxa += 1
                            families.append('ancylidae')
                    else:
                        # try:
                        if taxon.subclassis.subclassis.lower() == "oligochaeta":
                            if 'oligochaeta' in families:
                                pass
                            else:
                                bmwp_score += taxon.subclassis.bmwp_score
                                n_taxa += 1
                                families.append('oligochaeta')
                        # except AttributeError:
                        else:
                            if taxon.familia.familia in families or taxon.familia.bmwp_score is None:
                                continue
                            else:
                                bmwp_score += taxon.familia.bmwp_score
                                n_taxa += 1
                                families.append(taxon.familia.familia)
                if len(taxons) == 0:
                    return None
                else:
                    aspt = round(bmwp_score/n_taxa, 2)
                    bmwp = {'bmwp_score': bmwp_score,
                             'aspt': aspt,
                             'ntaxa': n_taxa}
                    return bmwp


            def whpt_aspt(csv_file):
                """Calculation of WHPT score"""
                whpt_score = 0
                whpt_ntaxa = 0
                ancylidae = ['ancylus fluviatilis', 'ancylus sp.', 'ancylidae',
                             'ancylidae/acroloxidae', '"ancylidae" gen. sp.']
                whpt = {}
                taxa_groups = {}
                taxons = []

                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon1 = Taxon.objects.get(taxon__iexact=row['taxon'])
                        taxons.append(taxon1)
                    # except ObjectDoesNotExist:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    # If abundance data is present
                    try:
                        abundance = int(row['abundance'])
                        # Generating the family dictionary for the purpose of counting abundance
                        if row['taxon'].lower() in ancylidae:
                            taxa_groups['Ancylidae'] = taxa_groups.get('Ancylidae', 0) + abundance
                        else:
                            try:
                                if taxon1.subclassis.subclassis.lower() == 'oligochaeta':
                                    taxa_groups['Oligochaeta'] = taxa_groups.get('Oligochaeta', 0) + abundance
                                else:
                                    taxa_groups[taxon1.familia] = taxa_groups.get(taxon1.familia, 0) + abundance
                            except AttributeError:
                                taxa_groups[taxon1.familia] = taxa_groups.get(taxon1.familia, 0) + abundance
                    # If abundance data is not present
                    except (AttributeError, KeyError, ValueError):
                        if row['taxon'].lower() in ancylidae:
                            try:
                                if taxa_groups['Ancylidae'] > 0:
                                    pass
                                else:
                                    taxa_groups['Ancylidae'] = 0
                            except KeyError:
                                taxa_groups['Ancylidae'] = taxa_groups.get('Ancylidae', 0)
                        else:
                            try:
                                if taxon1.subclassis.subclassis.lower() == 'oligochaeta':
                                    try:
                                        if taxa_groups['Oligochaeta'] > 0:
                                            pass
                                        else:
                                            taxa_groups['Oligochaeta'] = 0
                                    except KeyError:
                                        taxa_groups['Oligochaeta'] = taxa_groups.get('Oligochaeta', 0)
                                else:
                                    try:
                                        if taxa_groups[taxon1.familia] > 0:
                                            pass
                                        else:
                                            taxa_groups[taxon1.familia] = 0
                                    except KeyError:
                                        taxa_groups[taxon1.familia] = taxa_groups.get(taxon1.familia, 0)
                            except AttributeError:
                                try:
                                    if taxa_groups[taxon1.familia] > 0:
                                        pass
                                    else:
                                        taxa_groups[taxon1.familia] = 0
                                except KeyError:
                                    taxa_groups[taxon1.familia] = taxa_groups.get(taxon1.familia, 0)

                if len(taxons) == 0:
                    return None
                else:
                    for group, abund in taxa_groups.items():
                        if group == 'Ancylidae':
                            if abund >= 10:
                                whpt_score += 5.5
                                whpt_ntaxa += 1
                            elif abund >= 1:
                                whpt_score += 5.8
                                whpt_ntaxa += 1
                            else:
                                whpt_score += 5.7
                                whpt_ntaxa += 1
                        elif group == 'Oligochaeta':
                            try:
                                taxon2 = Subclass.objects.get(subclassis=group)
                            except ObjectDoesNotExist:
                                messages.error(request, 'Taxon not found in the database')
                                return redirect('index_calculator')
                            if abund >= 1000:
                                whpt_score += taxon2.subclassis.whpt_ab4
                                whpt_ntaxa += 1
                            elif abund >= 100:
                                whpt_score += taxon2.subclassis.whpt_ab3
                                whpt_ntaxa += 1
                            elif abund >= 10:
                                whpt_score += taxon2.whpt_ab2
                                whpt_ntaxa += 1
                            elif abund >= 1:
                                whpt_score += taxon2.whpt_ab1
                                whpt_ntaxa += 1
                            else:
                                whpt_score += taxon2.whpt_po
                                whpt_ntaxa += 1
                        else:
                            try:
                                taxon3 = Family.objects.get(familia=group)
                            except ObjectDoesNotExist:
                                messages.error(request,
                                               'Taxon not found in the database')
                                return redirect('index_calculator')
                            try:
                                if abund >= 1000:
                                    whpt_score += taxon3.whpt_ab4
                                    if taxon3.whpt_ab4 is None:
                                        pass
                                    else:
                                        whpt_ntaxa += 1
                                elif abund >= 100:
                                    whpt_score += taxon3.whpt_ab3
                                    if taxon3.whpt_ab3 is None:
                                        pass
                                    else:
                                        whpt_ntaxa += 1
                                elif abund >= 10:
                                    whpt_score += taxon3.whpt_ab2
                                    if taxon3.whpt_ab2 is None:
                                        pass
                                    else:
                                        whpt_ntaxa += 1
                                elif abund >= 1:
                                    whpt_score += taxon3.whpt_ab1
                                    if taxon3.whpt_ab1 is None:
                                        pass
                                    else:
                                        whpt_ntaxa += 1
                                else:
                                    whpt_score += taxon3.whpt_po
                                    if taxon3.whpt_po is None:
                                        pass
                                    else:
                                        whpt_ntaxa += 1
                            except TypeError:
                                pass

                        whpt_score = round(whpt_score, 2)
                        aspt = round(whpt_score/whpt_ntaxa, 2)
                        whpt = {'whpt_score': whpt_score,
                                 'aspt': aspt,
                                 'ntaxa': whpt_ntaxa}

                    return whpt


            def cc_index(csv_file):
                cs_values = []
                cs_sum = 0
                cci_ntaxa = 0
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist:
                    #     messages.error(request,
                    #                    'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    if taxon.cci_cs is None:
                        continue
                    else:
                        cs_sum += taxon.cci_cs
                        cci_ntaxa += 1
                        cs_values.append(taxon.cci_cs)

                if len(taxons) == 0:
                    return None
                else:
                    bmwp_value = bmwp['bmwp_score']
                    cs_max = max(cs_values)

                    if bmwp_value >= 301:
                        cos_bmwp = 15
                    elif bmwp_value >= 251:
                        cos_bmwp = 12
                    elif bmwp_value >= 201:
                        cos_bmwp = 10
                    elif bmwp_value >= 151:
                        cos_bmwp = 7
                    elif bmwp_value >= 101:
                        cos_bmwp = 5
                    elif bmwp_value >= 51:
                        cos_bmwp = 3
                    elif bmwp_value >= 1:
                        cos_bmwp = 1
                    else:
                        cos_bmwp = 0

                    if len(cs_values) < 1:
                        cos_cs = 0
                    else:
                        match cs_max:
                            case 10:
                                cos_cs = 15
                            case 9:
                                cos_cs = 12
                            case 8:
                                cos_cs = 10
                            case 7:
                                cos_cs = 7
                            case 5 | 6:
                                cos_cs = 5
                            case 3 | 4:
                                cos_cs = 3
                            case 1 | 2:
                                cos_cs = 1

                    if cos_bmwp > cos_cs:
                        cci = round((cs_sum / cci_ntaxa) * cos_bmwp, 2)
                    else:
                        cci = round((cs_sum / cci_ntaxa) * cos_cs, 2)

                    return cci


            def life_s(csv_file):
                ab = 0
                fs_sum = 0
                life_ntaxa = 0
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    try:
                        abundance = int(row['abundance'])
                    except (AttributeError, KeyError, ValueError):
                        continue
                    else:
                        match taxon.familia:
                            case 'Simuliidae' | 'Chaoboridae' | 'Culicidae':
                                try:
                                    fg = LifeScores.objects.get(flow_group=taxon.familia.life_fg)
                                except ObjectDoesNotExist:
                                    continue
                            case _:
                                try:
                                    fg = LifeScores.objects.get(flow_group=taxon.life_fg)
                                except ObjectDoesNotExist:
                                    continue
                        if abundance >= 1000:
                            fs_sum += fg.a_cat_de
                            life_ntaxa += 1
                            ab += abundance
                        elif abundance >= 100:
                            fs_sum += fg.a_cat_c
                            life_ntaxa += 1
                            ab += abundance
                        elif abundance >= 10:
                            fs_sum += fg.a_cat_b
                            life_ntaxa += 1
                            ab += abundance
                        elif abundance >= 1:
                            fs_sum += fg.a_cat_a
                            life_ntaxa += 1
                            ab += abundance

                if len(taxons) == 0:
                    return None
                else:
                    if ab > 0:
                        life = round(fs_sum/life_ntaxa, 2)
                        return life
                    else:
                        return None


            def life_f(csv_file):
                ab = 0
                fs_sum = 0
                life_ntaxa = 0
                ancylidae = ['ancylus fluviatilis', 'ancylus sp.', 'ancylidae',
                             'ancylidae/acroloxidae', '"ancylidae" gen. sp.']
                families = {}
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist or TypeError:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    try:
                        abundance = int(row['abundance'])
                    except (AttributeError, KeyError, ValueError):
                        continue
                    else:
                        if row['taxon'].lower() in ancylidae:
                            families['Ancylidae'] = families.get('Ancylidae', 0) + abundance
                            ab += abundance
                        else:
                            families[taxon.familia] = families.get(taxon.familia, 0) + abundance
                            ab += abundance

                if len(taxons) == 0:
                    return None
                else:
                    if ab == 0:
                        return None
                    else:
                        for fam, abund in families.items():
                            if fam == 'Ancylidae':
                                fg = LifeScores.objects.get(flow_group='II')
                            else:
                                try:
                                    fg = LifeScores.objects.get(flow_group=fam.life_fg)
                                except ObjectDoesNotExist:
                                    continue
                            if abund >= 1000:
                                fs_sum += fg.a_cat_de
                                life_ntaxa += 1
                            elif abund >= 100:
                                fs_sum += fg.a_cat_c
                                life_ntaxa += 1
                            elif abund >= 10:
                                fs_sum += fg.a_cat_b
                                life_ntaxa += 1
                            elif abund >= 1:
                                fs_sum += fg.a_cat_a
                                life_ntaxa += 1
                        life = round(fs_sum/life_ntaxa, 2)
                        return life


            def psi_s(csv_file):
                ab = 0
                sum_ab = 0
                sum_abcd = 0
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist or TypeError:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    try:
                        abundance = int(row['abundance'])
                    except (AttributeError, KeyError, ValueError):
                        continue
                    else:
                        try:
                            fssr = PsiScores.objects.get(fssr_group=taxon.psi_fssr)
                        except ObjectDoesNotExist:
                            continue
                        match taxon.psi_fssr:
                            case 'A' | 'B':
                                if abundance >= 1000:
                                    sum_ab += fssr.a_cat_d
                                    sum_abcd += fssr.a_cat_d
                                    ab += abundance
                                elif abundance >= 100:
                                    sum_ab += fssr.a_cat_c
                                    sum_abcd += fssr.a_cat_c
                                    ab += abundance
                                elif abundance >= 10:
                                    sum_ab += fssr.a_cat_b
                                    sum_abcd += fssr.a_cat_b
                                    ab += abundance
                                elif abundance >= 1:
                                    sum_ab += fssr.a_cat_a
                                    sum_abcd += fssr.a_cat_a
                                    ab += abundance
                            case 'C' | 'D':
                                if abundance >= 1000:
                                    sum_abcd += fssr.a_cat_d
                                    ab += abundance
                                elif abundance >= 100:
                                    sum_abcd += fssr.a_cat_c
                                    ab += abundance
                                elif abundance >= 10:
                                    sum_abcd += fssr.a_cat_b
                                    ab += abundance
                                elif abundance >= 1:
                                    sum_abcd += fssr.a_cat_a
                                ab += abundance

                if len(taxons) == 0:
                    return None
                else:
                    if ab == 0:
                        return None
                    else:
                        psi = round((sum_ab / sum_abcd) * 100, 2)
                        return psi


            def psi_f(csv_file):
                ab = 0
                sum_ab = 0
                sum_abcd = 0
                ancylidae = ['ancylus fluviatilis', 'ancylus sp.', 'ancylidae',
                             'ancylidae/acroloxidae', '"ancylidae" gen. sp.']
                families = {}
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist or TypeError:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    try:
                        abundance = int(row['abundance'])
                    except (AttributeError, KeyError, ValueError):
                        continue
                    else:
                        if row['taxon'].lower() in ancylidae:
                            families['Ancylidae'] = families.get('Ancylidae', 0) + abundance
                            ab += abundance
                        else:
                            families[taxon.familia] = families.get(taxon.familia, 0) + abundance
                            ab += abundance

                if len(taxons) == 0:
                    return None
                else:
                    if ab == 0:
                        return None
                    else:
                        for fam, abund in families.items():
                            if fam == 'Ancylidae':
                                fssr = PsiScores.objects.get(fssr_group='A')
                            else:
                                try:
                                    fssr = PsiScores.objects.get(fssr_group=fam.psi_fssr)
                                except ObjectDoesNotExist:
                                    continue
                            try:
                                match fam.psi_fssr:
                                    case 'A' | 'B':
                                        if abund >= 1000:
                                            sum_ab += fssr.a_cat_d
                                            sum_abcd += fssr.a_cat_d
                                        elif abund >= 100:
                                            sum_ab += fssr.a_cat_c
                                            sum_abcd += fssr.a_cat_c
                                        elif abund >= 10:
                                            sum_ab += fssr.a_cat_b
                                            sum_abcd += fssr.a_cat_b
                                        elif abund >= 1:
                                            sum_ab += fssr.a_cat_a
                                            sum_abcd += fssr.a_cat_a
                                    case 'C' | 'D':
                                        if abund >= 1000:
                                            sum_abcd += fssr.a_cat_d
                                        elif abund >= 100:
                                            sum_abcd += fssr.a_cat_c
                                        elif abund >= 10:
                                            sum_abcd += fssr.a_cat_b
                                        elif abund >= 1:
                                            sum_abcd += fssr.a_cat_a
                            except AttributeError:
                                continue
                        psi = round((sum_ab / sum_abcd) * 100, 2)
                        return psi


            def dehli_calc(csv_file):
                sum_dis = 0
                ntaxa = 0
                ancylidae = ['ancylus fluviatilis', 'ancylus sp.', 'ancylidae',
                             'ancylidae/acroloxidae', '"ancylidae" gen. sp.']
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    # else:

                    if row['taxon'].lower() in ancylidae:
                        continue
                    else:
                        try:
                            sum_dis += taxon.genus.dehli_dis
                            ntaxa += 1
                        except (TypeError, AttributeError, ObjectDoesNotExist):
                            try:
                                sum_dis += taxon.tribus.dehli_dis
                                ntaxa += 1
                            except (TypeError, AttributeError, ObjectDoesNotExist):
                                try:
                                    sum_dis += taxon.subfamilia.dehli_dis
                                    ntaxa += 1
                                except (TypeError, AttributeError, ObjectDoesNotExist):
                                    try:
                                        sum_dis += taxon.familia.dehli_dis
                                        ntaxa += 1
                                    except (TypeError, AttributeError, ObjectDoesNotExist):
                                        continue
                if len(taxons) == 0:
                    return None
                else:
                    dhl = round(sum_dis / ntaxa, 2)
                    return dhl


            def epsi_r(csv_file):
                ab = 0
                sum_sensitive = 0
                sum_all = 0
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    try:
                        abundance = int(row['abundance'])
                        if abundance >= 1000:
                            log_abundance = 4
                            ab += abundance
                        elif abundance >= 100:
                            log_abundance = 3
                            ab += abundance
                        elif abundance >= 10:
                            log_abundance = 2
                            ab += abundance
                        elif abundance >= 1:
                            log_abundance = 1
                            ab += abundance
                    except (AttributeError, KeyError, ValueError):
                        continue
                    else:
                        if not taxon.epsi_w_r:
                            continue
                        else:
                            w = taxon.epsi_w_r
                            if w >= 0.5:
                                sum_sensitive += w * log_abundance
                                sum_all += w * log_abundance
                            elif w < 0.5:
                                sum_all += w * log_abundance
                if len(taxons) == 0:
                    return None
                else:
                    if ab == 0:
                        return None
                    else:
                        epsi = round((sum_sensitive / sum_all) * 100, 2)
                        return epsi


            def epsi_p(csv_file):
                ab = 0
                sum_sensitive = 0
                sum_all = 0
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    # else:
                    try:
                        abundance = int(row['abundance'])
                    except (AttributeError, KeyError, ValueError):
                        continue
                    else:
                        if abundance >= 1000:
                            log_abundance = 4
                            ab += abundance
                        elif abundance >= 100:
                            log_abundance = 3
                            ab += abundance
                        elif abundance >= 10:
                            log_abundance = 2
                            ab += abundance
                        elif abundance >= 1:
                            log_abundance = 1
                            ab += abundance

                        if not taxon.epsi_w_p:
                            continue
                        else:
                            w = taxon.epsi_w_p
                            if w >= 0.5:
                                sum_sensitive += w * log_abundance
                                sum_all += w * log_abundance
                            elif w < 0.5:
                                sum_all += w * log_abundance
                if len(taxons) == 0:
                    return None
                else:
                    if ab ==0:
                        return None
                    else:
                        epsi = round((sum_sensitive / sum_all) * 100, 2)
                        return epsi


            def uk_bap(csv_file):
                no_ukbap = 0
                ukbap_species = ['aeshna isosceles', 'agabus brunneus', 'anisus vorticulus', 'austropotamobius pallipes',
                                 'bagous nodulosus', 'bidessus minutissimus', 'bidessus unistriatus', 'brachyptera putata',
                                 'campsicnemus magius', 'coenagrion mercuriale', 'donacia aquatica', 'donacia bicolora',
                                 'eristalis cryptarum', 'glossosoma intermedium', 'gyraulus acronicus', 'hagenella clathrata',
                                 'helophorus laticollis', 'hydrochus nitidicollis', 'hydrometra gracilenta',
                                 'hydroporus necopinatus roni', 'hydroporus rufifrons', 'hydropsyche bulgaromanorum',
                                 'ironoquia dubia', 'isogenus nubecula', 'laccophilus poecilus', 'lophopus crystallinus',
                                 'macrosteles cyane', 'margaritifera margaritifera', 'myxas glutinosa', 'nigrobaetis niger',
                                 'niphargus glenniei', 'ochthebius poweri', 'odontomyia hydroleon', 'omphiscola glabra',
                                 'pisidium tenuilineatum', 'potamanthus luteus', 'pseudanodonta complanata complanata',
                                 'segmentina nitida', 'sphaerium solidum', 'triops cancriformis', 'valvata macrostoma',
                                 'vertigo angustior', 'vertigo genesii', 'vertigo geyeri', 'vertigo moulinsiana'
                                 ]

                for row in csv.DictReader(csv_file):
                    if row['taxon'].lower() in ukbap_species:
                        no_ukbap += 1

                if no_ukbap == 0:
                    return '0'
                else:
                    return no_ukbap


            bmwp = bmwp_aspt(io_string_csv)
            io_string_csv.seek(0)

            whpt = whpt_aspt(io_string_csv)
            io_string_csv.seek(0)

            cci = cc_index(io_string_csv)
            io_string_csv.seek(0)

            lifesp = life_s(io_string_csv)
            io_string_csv.seek(0)

            lifef = life_f(io_string_csv)
            io_string_csv.seek(0)

            psis = psi_s(io_string_csv)
            io_string_csv.seek(0)

            psif = psi_f(io_string_csv)
            io_string_csv.seek(0)

            epsir = epsi_r(io_string_csv)
            io_string_csv.seek(0)

            epsip = epsi_p(io_string_csv)
            io_string_csv.seek(0)

            ukbap = uk_bap(io_string_csv)
            io_string_csv.seek(0)

            request.session['bmwp'] = bmwp
            request.session['whpt'] = whpt
            request.session['cci'] = cci
            request.session['lifesp'] = lifesp
            request.session['lifef'] = lifef
            request.session['psis'] = psis
            request.session['psif'] = psif
            request.session['epsir'] = epsir
            request.session['epsip'] = epsip
            request.session['ukbap'] = ukbap

            try:
                dehli = dehli_calc(io_string_dehli)
                io_string_dehli.seek(0)
                request.session['dehli'] = dehli
            except:
                pass

            return redirect('index_calculator')
