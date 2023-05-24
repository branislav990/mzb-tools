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
        bmwp1 = request.session.get('bmwp1', False)
        bmwp2 = request.session.get('bmwp2', False)
        bmwp3 = request.session.get('bmwp3', False)
        bmwp4 = request.session.get('bmwp4', False)
        bmwp5 = request.session.get('bmwp5', False)
        bmwp6 = request.session.get('bmwp6', False)
        bmwp7 = request.session.get('bmwp7', False)
        bmwp8 = request.session.get('bmwp8', False)
        bmwp9 = request.session.get('bmwp9', False)
        bmwp10 = request.session.get('bmwp10', False)

        whpt1 = request.session.get('whpt1', False)
        whpt2 = request.session.get('whpt2', False)
        whpt3 = request.session.get('whpt3', False)
        whpt4 = request.session.get('whpt4', False)
        whpt5 = request.session.get('whpt5', False)
        whpt6 = request.session.get('whpt6', False)
        whpt7 = request.session.get('whpt7', False)
        whpt8 = request.session.get('whpt8', False)
        whpt9 = request.session.get('whpt9', False)
        whpt10 = request.session.get('whpt10', False)

        cci1 = request.session.get('cci1', False)
        cci2 = request.session.get('cci2', False)
        cci3 = request.session.get('cci3', False)
        cci4 = request.session.get('cci4', False)
        cci5 = request.session.get('cci5', False)
        cci6 = request.session.get('cci6', False)
        cci7 = request.session.get('cci7', False)
        cci8 = request.session.get('cci8', False)
        cci9 = request.session.get('cci9', False)
        cci10 = request.session.get('cci10', False)

        lifesp1 = request.session.get('lifesp1', False)
        lifesp2 = request.session.get('lifesp2', False)
        lifesp3 = request.session.get('lifesp3', False)
        lifesp4 = request.session.get('lifesp4', False)
        lifesp5 = request.session.get('lifesp5', False)
        lifesp6 = request.session.get('lifesp6', False)
        lifesp7 = request.session.get('lifesp7', False)
        lifesp8 = request.session.get('lifesp8', False)
        lifesp9 = request.session.get('lifesp9', False)
        lifesp10 = request.session.get('lifesp10', False)

        lifef1 = request.session.get('lifef1', False)
        lifef2 = request.session.get('lifef2', False)
        lifef3 = request.session.get('lifef3', False)
        lifef4 = request.session.get('lifef4', False)
        lifef5 = request.session.get('lifef5', False)
        lifef6 = request.session.get('lifef6', False)
        lifef7 = request.session.get('lifef7', False)
        lifef8 = request.session.get('lifef8', False)
        lifef9 = request.session.get('lifef9', False)
        lifef10 = request.session.get('lifef10', False)

        psis1 = request.session.get('psis1', False)
        psis2 = request.session.get('psis2', False)
        psis3 = request.session.get('psis3', False)
        psis4 = request.session.get('psis4', False)
        psis5 = request.session.get('psis5', False)
        psis6 = request.session.get('psis6', False)
        psis7 = request.session.get('psis7', False)
        psis8 = request.session.get('psis8', False)
        psis9 = request.session.get('psis9', False)
        psis10 = request.session.get('psis10', False)

        psif1 = request.session.get('psif1', False)
        psif2 = request.session.get('psif2', False)
        psif3 = request.session.get('psif3', False)
        psif4 = request.session.get('psif4', False)
        psif5 = request.session.get('psif5', False)
        psif6 = request.session.get('psif6', False)
        psif7 = request.session.get('psif7', False)
        psif8 = request.session.get('psif8', False)
        psif9 = request.session.get('psif9', False)
        psif10 = request.session.get('psif10', False)

        dehli1 = request.session.get('dehli1', False)
        dehli2 = request.session.get('dehli2', False)
        dehli3 = request.session.get('dehli3', False)
        dehli4 = request.session.get('dehli4', False)
        dehli5 = request.session.get('dehli5', False)
        dehli6 = request.session.get('dehli6', False)
        dehli7 = request.session.get('dehli7', False)
        dehli8 = request.session.get('dehli8', False)
        dehli9 = request.session.get('dehli9', False)
        dehli10 = request.session.get('dehli10', False)

        epsir1 = request.session.get('epsir1', False)
        epsir2 = request.session.get('epsir2', False)
        epsir3 = request.session.get('epsir3', False)
        epsir4 = request.session.get('epsir4', False)
        epsir5 = request.session.get('epsir5', False)
        epsir6 = request.session.get('epsir6', False)
        epsir7 = request.session.get('epsir7', False)
        epsir8 = request.session.get('epsir8', False)
        epsir9 = request.session.get('epsir9', False)
        epsir10 = request.session.get('epsir10', False)

        epsip1 = request.session.get('epsip1', False)
        epsip2 = request.session.get('epsip2', False)
        epsip3 = request.session.get('epsip3', False)
        epsip4 = request.session.get('epsip4', False)
        epsip5 = request.session.get('epsip5', False)
        epsip6 = request.session.get('epsip6', False)
        epsip7 = request.session.get('epsip7', False)
        epsip8 = request.session.get('epsip8', False)
        epsip9 = request.session.get('epsip9', False)
        epsip10 = request.session.get('epsip10', False)

        ukbap1 = request.session.get('ukbap1', False)
        ukbap2 = request.session.get('ukbap2', False)
        ukbap3 = request.session.get('ukbap3', False)
        ukbap4 = request.session.get('ukbap4', False)
        ukbap5 = request.session.get('ukbap5', False)
        ukbap6 = request.session.get('ukbap6', False)
        ukbap7 = request.session.get('ukbap7', False)
        ukbap8 = request.session.get('ukbap8', False)
        ukbap9 = request.session.get('ukbap9', False)
        ukbap10 = request.session.get('ukbap10', False)

        site_date = request.session.get('site_date', False)

        if bmwp1:
            del (request.session['bmwp1'])
        if bmwp2:
            del (request.session['bmwp2'])
        if bmwp3:
            del (request.session['bmwp3'])
        if bmwp4:
            del (request.session['bmwp4'])
        if bmwp5:
            del (request.session['bmwp5'])
        if bmwp6:
            del (request.session['bmwp6'])
        if bmwp7:
            del (request.session['bmwp7'])
        if bmwp8:
            del (request.session['bmwp8'])
        if bmwp9:
            del (request.session['bmwp9'])
        if bmwp10:
            del (request.session['bmwp10'])

        if whpt1:
            del (request.session['whpt1'])
        if whpt2:
            del (request.session['whpt2'])
        if whpt3:
            del (request.session['whpt3'])
        if whpt4:
            del (request.session['whpt4'])
        if whpt5:
            del (request.session['whpt5'])
        if whpt6:
            del (request.session['whpt6'])
        if whpt7:
            del (request.session['whpt7'])
        if whpt8:
            del (request.session['whpt8'])
        if whpt9:
            del (request.session['whpt9'])
        if whpt10:
            del (request.session['whpt10'])

        if cci1:
            del (request.session['cci1'])
        if cci2:
            del (request.session['cci2'])
        if cci3:
            del (request.session['cci3'])
        if cci4:
            del (request.session['cci4'])
        if cci5:
            del (request.session['cci5'])
        if cci6:
            del (request.session['cci6'])
        if cci7:
            del (request.session['cci7'])
        if cci8:
            del (request.session['cci8'])
        if cci9:
            del (request.session['cci9'])
        if cci10:
            del (request.session['cci10'])

        if lifesp1:
            del (request.session['lifesp1'])
        if lifesp2:
            del (request.session['lifesp2'])
        if lifesp3:
            del (request.session['lifesp3'])
        if lifesp4:
            del (request.session['lifesp4'])
        if lifesp5:
            del (request.session['lifesp5'])
        if lifesp6:
            del (request.session['lifesp6'])
        if lifesp7:
            del (request.session['lifesp7'])
        if lifesp8:
            del (request.session['lifesp8'])
        if lifesp9:
            del (request.session['lifesp9'])
        if lifesp10:
            del (request.session['lifesp10'])

        if lifef1:
            del (request.session['lifef1'])
        if lifef2:
            del (request.session['lifef2'])
        if lifef3:
            del (request.session['lifef3'])
        if lifef4:
            del (request.session['lifef4'])
        if lifef5:
            del (request.session['lifef5'])
        if lifef6:
            del (request.session['lifef6'])
        if lifef7:
            del (request.session['lifef7'])
        if lifef8:
            del (request.session['lifef8'])
        if lifef9:
            del (request.session['lifef9'])
        if lifef10:
            del (request.session['lifef10'])

        if psis1:
            del (request.session['psis1'])
        if psis2:
            del (request.session['psis2'])
        if psis3:
            del (request.session['psis3'])
        if psis4:
            del (request.session['psis4'])
        if psis5:
            del (request.session['psis5'])
        if psis6:
            del (request.session['psis6'])
        if psis7:
            del (request.session['psis7'])
        if psis8:
            del (request.session['psis8'])
        if psis9:
            del (request.session['psis9'])
        if psis10:
            del (request.session['psis10'])

        if psif1:
            del (request.session['psif1'])
        if psif2:
            del (request.session['psif2'])
        if psif3:
            del (request.session['psif3'])
        if psif4:
            del (request.session['psif4'])
        if psif5:
            del (request.session['psif5'])
        if psif6:
            del (request.session['psif6'])
        if psif7:
            del (request.session['psif7'])
        if psif8:
            del (request.session['psif8'])
        if psif9:
            del (request.session['psif9'])
        if psif10:
            del (request.session['psif10'])

        if dehli1:
            del (request.session['dehli1'])
        if dehli2:
            del (request.session['dehli2'])
        if dehli3:
            del (request.session['dehli3'])
        if dehli4:
            del (request.session['dehli4'])
        if dehli5:
            del (request.session['dehli5'])
        if dehli6:
            del (request.session['dehli6'])
        if dehli7:
            del (request.session['dehli7'])
        if dehli8:
            del (request.session['dehli8'])
        if dehli9:
            del (request.session['dehli9'])
        if dehli10:
            del (request.session['dehli10'])

        if epsir1:
            del (request.session['epsir1'])
        if epsir2:
            del (request.session['epsir2'])
        if epsir3:
            del (request.session['epsir3'])
        if epsir4:
            del (request.session['epsir4'])
        if epsir5:
            del (request.session['epsir5'])
        if epsir6:
            del (request.session['epsir6'])
        if epsir7:
            del (request.session['epsir7'])
        if epsir8:
            del (request.session['epsir8'])
        if epsir9:
            del (request.session['epsir9'])
        if epsir10:
            del (request.session['epsir10'])

        if epsip1:
            del (request.session['epsip1'])
        if epsip2:
            del (request.session['epsip2'])
        if epsip3:
            del (request.session['epsip3'])
        if epsip4:
            del (request.session['epsip4'])
        if epsip5:
            del (request.session['epsip5'])
        if epsip6:
            del (request.session['epsip6'])
        if epsip7:
            del (request.session['epsip7'])
        if epsip8:
            del (request.session['epsip8'])
        if epsip9:
            del (request.session['epsip9'])
        if epsip10:
            del (request.session['epsip10'])

        if ukbap1:
            del (request.session['ukbap1'])
        if ukbap2:
            del (request.session['ukbap2'])
        if ukbap3:
            del (request.session['ukbap3'])
        if ukbap4:
            del (request.session['ukbap4'])
        if ukbap5:
            del (request.session['ukbap5'])
        if ukbap6:
            del (request.session['ukbap6'])
        if ukbap7:
            del (request.session['ukbap7'])
        if ukbap8:
            del (request.session['ukbap8'])
        if ukbap9:
            del (request.session['ukbap9'])
        if ukbap10:
            del (request.session['ukbap10'])

        if site_date:
            del (request.session['site_date'])

        form_csv = UploadFileForm()
        form_dehli = UploadDehliForm()
        context = {
            'form_csv': form_csv,
            'form_dehli': form_dehli,

            'site_date': site_date,

            'bmwp1': bmwp1,
            'bmwp2': bmwp2,
            'bmwp3': bmwp3,
            'bmwp4': bmwp4,
            'bmwp5': bmwp5,
            'bmwp6': bmwp6,
            'bmwp7': bmwp7,
            'bmwp8': bmwp8,
            'bmwp9': bmwp9,
            'bmwp10': bmwp10,

            'whpt1': whpt1,
            'whpt2': whpt2,
            'whpt3': whpt3,
            'whpt4': whpt4,
            'whpt5': whpt5,
            'whpt6': whpt6,
            'whpt7': whpt7,
            'whpt8': whpt8,
            'whpt9': whpt9,
            'whpt10': whpt10,

            'cci1': cci1,
            'cci2': cci2,
            'cci3': cci3,
            'cci4': cci4,
            'cci5': cci5,
            'cci6': cci6,
            'cci7': cci7,
            'cci8': cci8,
            'cci9': cci9,
            'cci10': cci10,

            'lifesp1': lifesp1,
            'lifesp2': lifesp2,
            'lifesp3': lifesp3,
            'lifesp4': lifesp4,
            'lifesp5': lifesp5,
            'lifesp6': lifesp6,
            'lifesp7': lifesp7,
            'lifesp8': lifesp8,
            'lifesp9': lifesp9,
            'lifesp10': lifesp10,

            'lifef1': lifef1,
            'lifef2': lifef2,
            'lifef3': lifef3,
            'lifef4': lifef4,
            'lifef5': lifef5,
            'lifef6': lifef6,
            'lifef7': lifef7,
            'lifef8': lifef8,
            'lifef9': lifef9,
            'lifef10': lifef10,

            'psis1': psis1,
            'psis2': psis2,
            'psis3': psis3,
            'psis4': psis4,
            'psis5': psis5,
            'psis6': psis6,
            'psis7': psis7,
            'psis8': psis8,
            'psis9': psis9,
            'psis10': psis10,

            'psif1': psif1,
            'psif2': psif2,
            'psif3': psif3,
            'psif4': psif4,
            'psif5': psif5,
            'psif6': psif6,
            'psif7': psif7,
            'psif8': psif8,
            'psif9': psif9,
            'psif10': psif10,

            'dehli1': dehli1,
            'dehli2': dehli2,
            'dehli3': dehli3,
            'dehli4': dehli4,
            'dehli5': dehli5,
            'dehli6': dehli6,
            'dehli7': dehli7,
            'dehli8': dehli8,
            'dehli9': dehli9,
            'dehli10': dehli10,

            'epsir1': epsir1,
            'epsir2': epsir2,
            'epsir3': epsir3,
            'epsir4': epsir4,
            'epsir5': epsir5,
            'epsir6': epsir6,
            'epsir7': epsir7,
            'epsir8': epsir8,
            'epsir9': epsir9,
            'epsir10': epsir10,

            'epsip1': epsip1,
            'epsip2': epsip2,
            'epsip3': epsip3,
            'epsip4': epsip4,
            'epsip5': epsip5,
            'epsip6': epsip6,
            'epsip7': epsip7,
            'epsip8': epsip8,
            'epsip9': epsip9,
            'epsip10': epsip10,

            'ukbap1': ukbap1,
            'ukbap2': ukbap2,
            'ukbap3': ukbap3,
            'ukbap4': ukbap4,
            'ukbap5': ukbap5,
            'ukbap6': ukbap6,
            'ukbap7': ukbap7,
            'ukbap8': ukbap8,
            'ukbap9': ukbap9,
            'ukbap10': ukbap10
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


            def bmwp_aspt_1(csv_file):
                """Calculation of BMWP score and ASPT"""
                n_taxa = 0
                bmwp_score = 0
                families = []
                taxons = []
                ancylidae = ['ancylus fluviatilis', 'ancylus sp.', 'ancylidae',
                             'ancylidae/acroloxidae', '"ancylidae" gen. sp.']
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-1']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-1'])
                        taxons.append(taxon)
                    # except (ObjectDoesNotExist, TypeError):
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    # Ancylidae used to be a separate family, now they belong
                    # to Planorbide, but their BMWP score values differ
                    if row['taxon-1'].lower() in ancylidae:
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
                    bmwp1 = {'bmwp_score': bmwp_score,
                             'aspt': aspt,
                             'ntaxa': n_taxa}
                    return bmwp1

            def bmwp_aspt_2(csv_file):
                """Calculation of BMWP score and ASPT"""
                n_taxa = 0
                bmwp_score = 0
                families = []
                taxons = []
                ancylidae = ['ancylus fluviatilis', 'ancylus sp.', 'ancylidae',
                             'ancylidae/acroloxidae', '"ancylidae" gen. sp.']
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-2']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-2'])
                        taxons.append(taxon)
                    # except (ObjectDoesNotExist, TypeError):
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    # Ancylidae used to be a separate family, now they belong
                    # to Planorbide, but their BMWP score values differ
                    if row['taxon-2'].lower() in ancylidae:
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
                    bmwp2 = {'bmwp_score': bmwp_score,
                             'aspt': aspt,
                             'ntaxa': n_taxa}
                    return bmwp2

            def bmwp_aspt_3(csv_file):
                """Calculation of BMWP score and ASPT"""
                n_taxa = 0
                bmwp_score = 0
                families = []
                taxons = []
                ancylidae = ['ancylus fluviatilis', 'ancylus sp.', 'ancylidae',
                             'ancylidae/acroloxidae', '"ancylidae" gen. sp.']
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-3']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-3'])
                        taxons.append(taxon)
                    # except (ObjectDoesNotExist, TypeError):
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    # Ancylidae used to be a separate family, now they belong
                    # to Planorbide, but their BMWP score values differ
                    if row['taxon-3'].lower() in ancylidae:
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
                    bmwp3 = {'bmwp_score': bmwp_score,
                             'aspt': aspt,
                             'ntaxa': n_taxa}
                    return bmwp3

            def bmwp_aspt_4(csv_file):
                """Calculation of BMWP score and ASPT"""
                n_taxa = 0
                bmwp_score = 0
                families = []
                taxons = []
                ancylidae = ['ancylus fluviatilis', 'ancylus sp.', 'ancylidae',
                             'ancylidae/acroloxidae', '"ancylidae" gen. sp.']
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-4']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-4'])
                        taxons.append(taxon)
                    # except (ObjectDoesNotExist, TypeError):
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    # Ancylidae used to be a separate family, now they belong
                    # to Planorbide, but their BMWP score values differ
                    if row['taxon-4'].lower() in ancylidae:
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
                    bmwp4 = {'bmwp_score': bmwp_score,
                             'aspt': aspt,
                             'ntaxa': n_taxa}
                    return bmwp4

            def bmwp_aspt_5(csv_file):
                """Calculation of BMWP score and ASPT"""
                n_taxa = 0
                bmwp_score = 0
                families = []
                taxons = []
                ancylidae = ['ancylus fluviatilis', 'ancylus sp.', 'ancylidae',
                             'ancylidae/acroloxidae', '"ancylidae" gen. sp.']
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-5']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-5'])
                        taxons.append(taxon)
                    # except (ObjectDoesNotExist, TypeError):
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    # Ancylidae used to be a separate family, now they belong
                    # to Planorbide, but their BMWP score values differ
                    if row['taxon-5'].lower() in ancylidae:
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
                    bmwp5 = {'bmwp_score': bmwp_score,
                             'aspt': aspt,
                             'ntaxa': n_taxa}
                    return bmwp5

            def bmwp_aspt_6(csv_file):
                """Calculation of BMWP score and ASPT"""
                n_taxa = 0
                bmwp_score = 0
                families = []
                taxons = []
                ancylidae = ['ancylus fluviatilis', 'ancylus sp.', 'ancylidae',
                             'ancylidae/acroloxidae', '"ancylidae" gen. sp.']
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-6']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-6'])
                        taxons.append(taxon)
                    # except (ObjectDoesNotExist, TypeError):
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    # Ancylidae used to be a separate family, now they belong
                    # to Planorbide, but their BMWP score values differ
                    if row['taxon-6'].lower() in ancylidae:
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
                    bmwp6 = {'bmwp_score': bmwp_score,
                             'aspt': aspt,
                             'ntaxa': n_taxa}
                    return bmwp6

            def bmwp_aspt_7(csv_file):
                """Calculation of BMWP score and ASPT"""
                n_taxa = 0
                bmwp_score = 0
                families = []
                taxons = []
                ancylidae = ['ancylus fluviatilis', 'ancylus sp.', 'ancylidae',
                             'ancylidae/acroloxidae', '"ancylidae" gen. sp.']
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-7']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-7'])
                        taxons.append(taxon)
                    # except (ObjectDoesNotExist, TypeError):
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    # Ancylidae used to be a separate family, now they belong
                    # to Planorbide, but their BMWP score values differ
                    if row['taxon-7'].lower() in ancylidae:
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
                    bmwp7 = {'bmwp_score': bmwp_score,
                             'aspt': aspt,
                             'ntaxa': n_taxa}
                    return bmwp7

            def bmwp_aspt_8(csv_file):
                """Calculation of BMWP score and ASPT"""
                n_taxa = 0
                bmwp_score = 0
                families = []
                taxons = []
                ancylidae = ['ancylus fluviatilis', 'ancylus sp.', 'ancylidae',
                             'ancylidae/acroloxidae', '"ancylidae" gen. sp.']
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-8']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-8'])
                        taxons.append(taxon)
                    # except (ObjectDoesNotExist, TypeError):
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    # Ancylidae used to be a separate family, now they belong
                    # to Planorbide, but their BMWP score values differ
                    if row['taxon-8'].lower() in ancylidae:
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
                    bmwp8 = {'bmwp_score': bmwp_score,
                             'aspt': aspt,
                             'ntaxa': n_taxa}
                    return bmwp8

            def bmwp_aspt_9(csv_file):
                """Calculation of BMWP score and ASPT"""
                n_taxa = 0
                bmwp_score = 0
                families = []
                taxons = []
                ancylidae = ['ancylus fluviatilis', 'ancylus sp.', 'ancylidae',
                             'ancylidae/acroloxidae', '"ancylidae" gen. sp.']
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-9']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-9'])
                        taxons.append(taxon)
                    # except (ObjectDoesNotExist, TypeError):
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    # Ancylidae used to be a separate family, now they belong
                    # to Planorbide, but their BMWP score values differ
                    if row['taxon-9'].lower() in ancylidae:
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
                    bmwp9 = {'bmwp_score': bmwp_score,
                             'aspt': aspt,
                             'ntaxa': n_taxa}
                    return bmwp9

            def bmwp_aspt_10(csv_file):
                """Calculation of BMWP score and ASPT"""
                n_taxa = 0
                bmwp_score = 0
                families = []
                taxons = []
                ancylidae = ['ancylus fluviatilis', 'ancylus sp.', 'ancylidae',
                             'ancylidae/acroloxidae', '"ancylidae" gen. sp.']
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-10']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-10'])
                        taxons.append(taxon)
                    # except (ObjectDoesNotExist, TypeError):
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    # Ancylidae used to be a separate family, now they belong
                    # to Planorbide, but their BMWP score values differ
                    if row['taxon-10'].lower() in ancylidae:
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
                    bmwp10 = {'bmwp_score': bmwp_score,
                              'aspt': aspt,
                              'ntaxa': n_taxa}
                    return bmwp10


            def whpt_aspt_1(csv_file):
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
                        if not Taxon.objects.get(taxon__iexact=row['taxon-1']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon1 = Taxon.objects.get(taxon__iexact=row['taxon-1'])
                        taxons.append(taxon1)
                    # except ObjectDoesNotExist:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    # If abundance data is present
                    try:
                        abundance = int(row['abundance-1'])
                        # Generating the family dictionary for the purpose of counting abundance
                        if row['taxon-1'].lower() in ancylidae:
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
                        if row['taxon-1'].lower() in ancylidae:
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
                        whpt1 = {'whpt_score': whpt_score,
                                 'aspt': aspt,
                                 'ntaxa': whpt_ntaxa}

                    return whpt1

            def whpt_aspt_2(csv_file):
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
                        if not Taxon.objects.get(taxon__iexact=row['taxon-2']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon1 = Taxon.objects.get(taxon__iexact=row['taxon-2'])
                        taxons.append(taxon1)
                    # except ObjectDoesNotExist:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    # If abundance data is present
                    try:
                        abundance = int(row['abundance-2'])
                        # Generating the family dictionary for the purpose of counting abundance
                        if row['taxon-2'].lower() in ancylidae:
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
                        if row['taxon-2'].lower() in ancylidae:
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
                        whpt2 = {'whpt_score': whpt_score,
                                 'aspt': aspt,
                                 'ntaxa': whpt_ntaxa}

                    return whpt2

            def whpt_aspt_3(csv_file):
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
                        if not Taxon.objects.get(taxon__iexact=row['taxon-3']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon1 = Taxon.objects.get(taxon__iexact=row['taxon-3'])
                        taxons.append(taxon1)
                    # except ObjectDoesNotExist:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    # If abundance data is present
                    try:
                        abundance = int(row['abundance-3'])
                        # Generating the family dictionary for the purpose of counting abundance
                        if row['taxon-3'].lower() in ancylidae:
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
                        if row['taxon-3'].lower() in ancylidae:
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
                        whpt3 = {'whpt_score': whpt_score,
                                 'aspt': aspt,
                                 'ntaxa': whpt_ntaxa}

                    return whpt3

            def whpt_aspt_4(csv_file):
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
                        if not Taxon.objects.get(taxon__iexact=row['taxon-4']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon1 = Taxon.objects.get(taxon__iexact=row['taxon-4'])
                        taxons.append(taxon1)
                    # except ObjectDoesNotExist:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    # If abundance data is present
                    try:
                        abundance = int(row['abundance-4'])
                        # Generating the family dictionary for the purpose of counting abundance
                        if row['taxon-4'].lower() in ancylidae:
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
                        if row['taxon-4'].lower() in ancylidae:
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
                        whpt4 = {'whpt_score': whpt_score,
                                 'aspt': aspt,
                                 'ntaxa': whpt_ntaxa}

                    return whpt4

            def whpt_aspt_5(csv_file):
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
                        if not Taxon.objects.get(taxon__iexact=row['taxon-5']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon1 = Taxon.objects.get(taxon__iexact=row['taxon-5'])
                        taxons.append(taxon1)
                    # except ObjectDoesNotExist:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    # If abundance data is present
                    try:
                        abundance = int(row['abundance-5'])
                        # Generating the family dictionary for the purpose of counting abundance
                        if row['taxon-5'].lower() in ancylidae:
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
                        if row['taxon-5'].lower() in ancylidae:
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
                        whpt5 = {'whpt_score': whpt_score,
                                 'aspt': aspt,
                                 'ntaxa': whpt_ntaxa}

                    return whpt5

            def whpt_aspt_6(csv_file):
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
                        if not Taxon.objects.get(taxon__iexact=row['taxon-6']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon1 = Taxon.objects.get(taxon__iexact=row['taxon-6'])
                        taxons.append(taxon1)
                    # except ObjectDoesNotExist:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    # If abundance data is present
                    try:
                        abundance = int(row['abundance-6'])
                        # Generating the family dictionary for the purpose of counting abundance
                        if row['taxon-6'].lower() in ancylidae:
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
                        if row['taxon-6'].lower() in ancylidae:
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
                        whpt6 = {'whpt_score': whpt_score,
                                 'aspt': aspt,
                                 'ntaxa': whpt_ntaxa}

                    return whpt6

            def whpt_aspt_7(csv_file):
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
                        if not Taxon.objects.get(taxon__iexact=row['taxon-7']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon1 = Taxon.objects.get(taxon__iexact=row['taxon-7'])
                        taxons.append(taxon1)
                    # except ObjectDoesNotExist:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')

                    # If abundance data is present
                    try:
                        abundance = int(row['abundance-7'])
                        # Generating the family dictionary for the purpose of counting abundance
                        if row['taxon-7'].lower() in ancylidae:
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
                        if row['taxon-7'].lower() in ancylidae:
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
                        whpt7 = {'whpt_score': whpt_score,
                                 'aspt': aspt,
                                 'ntaxa': whpt_ntaxa}

                    return whpt7

            def whpt_aspt_8(csv_file):
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
                        if not Taxon.objects.get(taxon__iexact=row['taxon-8']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon1 = Taxon.objects.get(taxon__iexact=row['taxon-8'])
                        taxons.append(taxon1)
                    # except ObjectDoesNotExist:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')

                    # If abundance data is present
                    try:
                        abundance = int(row['abundance-8'])
                        # Generating the family dictionary for the purpose of counting abundance
                        if row['taxon-8'].lower() in ancylidae:
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
                        if row['taxon-8'].lower() in ancylidae:
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
                        whpt8 = {'whpt_score': whpt_score,
                                 'aspt': aspt,
                                 'ntaxa': whpt_ntaxa}
                        request.session['whpt'] = whpt

                    return whpt8

            def whpt_aspt_9(csv_file):
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
                        if not Taxon.objects.get(taxon__iexact=row['taxon-9']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon1 = Taxon.objects.get(taxon__iexact=row['taxon-9'])
                        taxons.append(taxon1)
                    # except ObjectDoesNotExist:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')

                    # If abundance data is present
                    try:
                        abundance = int(row['abundance-9'])
                        # Generating the family dictionary for the purpose of counting abundance
                        if row['taxon-9'].lower() in ancylidae:
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
                        if row['taxon-9'].lower() in ancylidae:
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
                        whpt9 = {'whpt_score': whpt_score,
                                 'aspt': aspt,
                                 'ntaxa': whpt_ntaxa}

                    return whpt9

            def whpt_aspt_10(csv_file):
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
                        if not Taxon.objects.get(taxon__iexact=row['taxon-10']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon1 = Taxon.objects.get(taxon__iexact=row['taxon-10'])
                        taxons.append(taxon1)
                    # except ObjectDoesNotExist:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')

                    # If abundance data is present
                    try:
                        abundance = int(row['abundance-10'])
                        # Generating the family dictionary for the purpose of counting abundance
                        if row['taxon-10'].lower() in ancylidae:
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
                        if row['taxon-10'].lower() in ancylidae:
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
                        whpt10 = {'whpt_score': whpt_score,
                                  'aspt': aspt,
                                  'ntaxa': whpt_ntaxa}

                    return whpt10


            def cc_index_1(csv_file):
                cs_values = []
                cs_sum = 0
                cci_ntaxa = 0
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-1']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-1'])
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
                    bmwp_value = bmwp1['bmwp_score']
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

            def cc_index_2(csv_file):
                cs_values = []
                cs_sum = 0
                cci_ntaxa = 0
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-2']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-2'])
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
                    bmwp_value = bmwp2['bmwp_score']
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

            def cc_index_3(csv_file):
                cs_values = []
                cs_sum = 0
                cci_ntaxa = 0
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-3']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-3'])
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
                    bmwp_value = bmwp3['bmwp_score']
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

            def cc_index_4(csv_file):
                cs_values = []
                cs_sum = 0
                cci_ntaxa = 0
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-4']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-4'])
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
                    bmwp_value = bmwp4['bmwp_score']
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

            def cc_index_5(csv_file):
                cs_values = []
                cs_sum = 0
                cci_ntaxa = 0
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-5']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-5'])
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
                    bmwp_value = bmwp5['bmwp_score']
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

            def cc_index_6(csv_file):
                cs_values = []
                cs_sum = 0
                cci_ntaxa = 0
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-6']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-6'])
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
                    bmwp_value = bmwp6['bmwp_score']
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

            def cc_index_7(csv_file):
                cs_values = []
                cs_sum = 0
                cci_ntaxa = 0
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-7']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-7'])
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
                    bmwp_value = bmwp7['bmwp_score']
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

            def cc_index_8(csv_file):
                cs_values = []
                cs_sum = 0
                cci_ntaxa = 0
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-8']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-8'])
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
                    bmwp_value = bmwp8['bmwp_score']
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

            def cc_index_9(csv_file):
                cs_values = []
                cs_sum = 0
                cci_ntaxa = 0
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-9']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-9'])
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
                    bmwp_value = bmwp9['bmwp_score']
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

            def cc_index_10(csv_file):
                cs_values = []
                cs_sum = 0
                cci_ntaxa = 0
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-10']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-10'])
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
                    bmwp_value = bmwp10['bmwp_score']
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


            def life_s_1(csv_file):
                ab = 0
                fs_sum = 0
                life_ntaxa = 0
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-1']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-1'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    try:
                        abundance = int(row['abundance-1'])
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

            def life_s_2(csv_file):
                ab = 0
                fs_sum = 0
                life_ntaxa = 0
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-2']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-2'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    try:
                        abundance = int(row['abundance-2'])
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

            def life_s_3(csv_file):
                ab = 0
                fs_sum = 0
                life_ntaxa = 0
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-3']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-3'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    try:
                        abundance = int(row['abundance-3'])
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

            def life_s_4(csv_file):
                ab = 0
                fs_sum = 0
                life_ntaxa = 0
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-4']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-4'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    try:
                        abundance = int(row['abundance-4'])
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

            def life_s_5(csv_file):
                ab = 0
                fs_sum = 0
                life_ntaxa = 0
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-5']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-5'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    try:
                        abundance = int(row['abundance-5'])
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

            def life_s_6(csv_file):
                ab = 0
                fs_sum = 0
                life_ntaxa = 0
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-6']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-6'])
                    taxons.append(taxon)
                    # except ObjectDoesNotExist:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    try:
                        abundance = int(row['abundance-6'])
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

            def life_s_7(csv_file):
                ab = 0
                fs_sum = 0
                life_ntaxa = 0
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-7']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-7'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    try:
                        abundance = int(row['abundance-7'])
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

            def life_s_8(csv_file):
                ab = 0
                fs_sum = 0
                life_ntaxa = 0
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-8']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-8'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    try:
                        abundance = int(row['abundance-8'])
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

            def life_s_9(csv_file):
                ab = 0
                fs_sum = 0
                life_ntaxa = 0
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-9']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-9'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    try:
                        abundance = int(row['abundance-9'])
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

            def life_s_10(csv_file):
                ab = 0
                fs_sum = 0
                life_ntaxa = 0
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-10']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-10'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    try:
                        abundance = int(row['abundance-10'])
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


            def life_f_1(csv_file):
                ab = 0
                fs_sum = 0
                life_ntaxa = 0
                ancylidae = ['ancylus fluviatilis', 'ancylus sp.', 'ancylidae',
                             'ancylidae/acroloxidae', '"ancylidae" gen. sp.']
                families = {}
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-1']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-1'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist or TypeError:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    try:
                        abundance = int(row['abundance-1'])
                    except (AttributeError, KeyError, ValueError):
                        continue
                    else:
                        if row['taxon-1'].lower() in ancylidae:
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

            def life_f_2(csv_file):
                ab = 0
                fs_sum = 0
                life_ntaxa = 0
                ancylidae = ['ancylus fluviatilis', 'ancylus sp.', 'ancylidae',
                             'ancylidae/acroloxidae', '"ancylidae" gen. sp.']
                families = {}
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-2']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-2'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist or TypeError:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    try:
                        abundance = int(row['abundance-2'])
                    except (AttributeError, KeyError, ValueError):
                        continue
                    else:
                        if row['taxon-2'].lower() in ancylidae:
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

            def life_f_3(csv_file):
                ab = 0
                fs_sum = 0
                life_ntaxa = 0
                ancylidae = ['ancylus fluviatilis', 'ancylus sp.', 'ancylidae',
                             'ancylidae/acroloxidae', '"ancylidae" gen. sp.']
                families = {}
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-3']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-3'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist or TypeError:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    try:
                        abundance = int(row['abundance-3'])
                    except (AttributeError, KeyError, ValueError):
                        continue
                    else:
                        if row['taxon-3'].lower() in ancylidae:
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

            def life_f_4(csv_file):
                ab = 0
                fs_sum = 0
                life_ntaxa = 0
                ancylidae = ['ancylus fluviatilis', 'ancylus sp.', 'ancylidae',
                             'ancylidae/acroloxidae', '"ancylidae" gen. sp.']
                families = {}
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-4']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-4'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist or TypeError:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    try:
                        abundance = int(row['abundance-4'])
                    except (AttributeError, KeyError, ValueError):
                        continue
                    else:
                        if row['taxon-4'].lower() in ancylidae:
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

            def life_f_5(csv_file):
                ab = 0
                fs_sum = 0
                life_ntaxa = 0
                ancylidae = ['ancylus fluviatilis', 'ancylus sp.', 'ancylidae',
                             'ancylidae/acroloxidae', '"ancylidae" gen. sp.']
                families = {}
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-5']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-5'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist or TypeError:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    try:
                        abundance = int(row['abundance-5'])
                    except (AttributeError, KeyError, ValueError):
                        continue
                    else:
                        if row['taxon-5'].lower() in ancylidae:
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

            def life_f_6(csv_file):
                ab = 0
                fs_sum = 0
                life_ntaxa = 0
                taxons = []
                ancylidae = ['ancylus fluviatilis', 'ancylus sp.', 'ancylidae',
                             'ancylidae/acroloxidae', '"ancylidae" gen. sp.']
                families = {}
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-6']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-6'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist or TypeError:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    try:
                        abundance = int(row['abundance-6'])
                    except (AttributeError, KeyError, ValueError):
                        continue
                    else:
                        if row['taxon-6'].lower() in ancylidae:
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

            def life_f_7(csv_file):
                ab = 0
                fs_sum = 0
                life_ntaxa = 0
                ancylidae = ['ancylus fluviatilis', 'ancylus sp.', 'ancylidae',
                             'ancylidae/acroloxidae', '"ancylidae" gen. sp.']
                families = {}
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-7']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-7'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist or TypeError:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    try:
                        abundance = int(row['abundance-7'])
                    except (AttributeError, KeyError, ValueError):
                        continue
                    else:
                        if row['taxon-7'].lower() in ancylidae:
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

            def life_f_8(csv_file):
                ab = 0
                fs_sum = 0
                life_ntaxa = 0
                ancylidae = ['ancylus fluviatilis', 'ancylus sp.', 'ancylidae',
                             'ancylidae/acroloxidae', '"ancylidae" gen. sp.']
                families = {}
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-8']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-8'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist or TypeError:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    try:
                        abundance = int(row['abundance-8'])
                    except (AttributeError, KeyError, ValueError):
                        continue
                    else:
                        if row['taxon-8'].lower() in ancylidae:
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

            def life_f_9(csv_file):
                ab = 0
                fs_sum = 0
                life_ntaxa = 0
                ancylidae = ['ancylus fluviatilis', 'ancylus sp.', 'ancylidae',
                             'ancylidae/acroloxidae', '"ancylidae" gen. sp.']
                families = {}
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-9']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-9'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist or TypeError:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    try:
                        abundance = int(row['abundance-9'])
                    except (AttributeError, KeyError, ValueError):
                        continue
                    else:
                        if row['taxon-9'].lower() in ancylidae:
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

            def life_f_10(csv_file):
                ab = 0
                fs_sum = 0
                life_ntaxa = 0
                ancylidae = ['ancylus fluviatilis', 'ancylus sp.', 'ancylidae',
                             'ancylidae/acroloxidae', '"ancylidae" gen. sp.']
                families = {}
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-10']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-10'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist or TypeError:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    try:
                        abundance = int(row['abundance-10'])
                    except (AttributeError, KeyError, ValueError):
                        continue
                    else:
                        if row['taxon-10'].lower() in ancylidae:
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


            def psi_s_1(csv_file):
                ab = 0
                sum_ab = 0
                sum_abcd = 0
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-1']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-1'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist or TypeError:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    try:
                        abundance = int(row['abundance-1'])
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

            def psi_s_2(csv_file):
                ab = 0
                sum_ab = 0
                sum_abcd = 0
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-2']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-2'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist or TypeError:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    try:
                        abundance = int(row['abundance-2'])
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

            def psi_s_3(csv_file):
                ab = 0
                sum_ab = 0
                sum_abcd = 0
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-3']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-3'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist or TypeError:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    try:
                        abundance = int(row['abundance-3'])
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

            def psi_s_4(csv_file):
                ab = 0
                sum_ab = 0
                sum_abcd = 0
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-4']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-4'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist or TypeError:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    try:
                        abundance = int(row['abundance-4'])
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

            def psi_s_5(csv_file):
                ab = 0
                sum_ab = 0
                sum_abcd = 0
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-5']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-5'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist or TypeError:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    try:
                        abundance = int(row['abundance-5'])
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

            def psi_s_6(csv_file):
                ab = 0
                sum_ab = 0
                sum_abcd = 0
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-6']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-6'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist or TypeError:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    try:
                        abundance = int(row['abundance-6'])
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

            def psi_s_7(csv_file):
                ab = 0
                sum_ab = 0
                sum_abcd = 0
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-7']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-7'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist or TypeError:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    try:
                        abundance = int(row['abundance-7'])
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

            def psi_s_8(csv_file):
                ab = 0
                sum_ab = 0
                sum_abcd = 0
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-8']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-8'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist or TypeError:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    try:
                        abundance = int(row['abundance-8'])
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

            def psi_s_9(csv_file):
                ab = 0
                sum_ab = 0
                sum_abcd = 0
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-9']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-9'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist or TypeError:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    try:
                        abundance = int(row['abundance-9'])
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

            def psi_s_10(csv_file):
                ab = 0
                sum_ab = 0
                sum_abcd = 0
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-10']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-10'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist or TypeError:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    try:
                        abundance = int(row['abundance-10'])
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


            def psi_f_1(csv_file):
                ab = 0
                sum_ab = 0
                sum_abcd = 0
                ancylidae = ['ancylus fluviatilis', 'ancylus sp.', 'ancylidae',
                             'ancylidae/acroloxidae', '"ancylidae" gen. sp.']
                families = {}
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-1']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-1'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist or TypeError:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    try:
                        abundance = int(row['abundance-1'])
                    except (AttributeError, KeyError, ValueError):
                        continue
                    else:
                        if row['taxon-1'].lower() in ancylidae:
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

            def psi_f_2(csv_file):
                ab = 0
                sum_ab = 0
                sum_abcd = 0
                ancylidae = ['ancylus fluviatilis', 'ancylus sp.', 'ancylidae',
                             'ancylidae/acroloxidae', '"ancylidae" gen. sp.']
                families = {}
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-2']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-2'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist or TypeError:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    try:
                        abundance = int(row['abundance-2'])
                    except (AttributeError, KeyError, ValueError):
                        continue
                    else:
                        if row['taxon-2'].lower() in ancylidae:
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

            def psi_f_3(csv_file):
                ab = 0
                sum_ab = 0
                sum_abcd = 0
                ancylidae = ['ancylus fluviatilis', 'ancylus sp.', 'ancylidae',
                             'ancylidae/acroloxidae', '"ancylidae" gen. sp.']
                families = {}
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-3']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-3'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist or TypeError:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    try:
                        abundance = int(row['abundance-3'])
                    except (AttributeError, KeyError, ValueError):
                        continue
                    else:
                        if row['taxon-3'].lower() in ancylidae:
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

            def psi_f_4(csv_file):
                ab = 0
                sum_ab = 0
                sum_abcd = 0
                ancylidae = ['ancylus fluviatilis', 'ancylus sp.', 'ancylidae',
                             'ancylidae/acroloxidae', '"ancylidae" gen. sp.']
                families = {}
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-4']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-4'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist or TypeError:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    try:
                        abundance = int(row['abundance-4'])
                    except (AttributeError, KeyError, ValueError):
                        continue
                    else:
                        if row['taxon-4'].lower() in ancylidae:
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

            def psi_f_5(csv_file):
                ab = 0
                sum_ab = 0
                sum_abcd = 0
                ancylidae = ['ancylus fluviatilis', 'ancylus sp.', 'ancylidae',
                             'ancylidae/acroloxidae', '"ancylidae" gen. sp.']
                families = {}
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-5']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-5'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist or TypeError:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    try:
                        abundance = int(row['abundance-5'])
                    except (AttributeError, KeyError, ValueError):
                        continue
                    else:
                        if row['taxon-5'].lower() in ancylidae:
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

            def psi_f_6(csv_file):
                ab = 0
                sum_ab = 0
                sum_abcd = 0
                ancylidae = ['ancylus fluviatilis', 'ancylus sp.', 'ancylidae',
                             'ancylidae/acroloxidae', '"ancylidae" gen. sp.']
                families = {}
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-6']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-6'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist or TypeError:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    try:
                        abundance = int(row['abundance-6'])
                    except (AttributeError, KeyError, ValueError):
                        continue
                    else:
                        if row['taxon-6'].lower() in ancylidae:
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

            def psi_f_7(csv_file):
                ab = 0
                sum_ab = 0
                sum_abcd = 0
                ancylidae = ['ancylus fluviatilis', 'ancylus sp.', 'ancylidae',
                             'ancylidae/acroloxidae', '"ancylidae" gen. sp.']
                families = {}
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-7']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-7'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist or TypeError:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    try:
                        abundance = int(row['abundance-7'])
                    except (AttributeError, KeyError, ValueError):
                        continue
                    else:
                        if row['taxon-7'].lower() in ancylidae:
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

            def psi_f_8(csv_file):
                ab = 0
                sum_ab = 0
                sum_abcd = 0
                ancylidae = ['ancylus fluviatilis', 'ancylus sp.', 'ancylidae',
                             'ancylidae/acroloxidae', '"ancylidae" gen. sp.']
                families = {}
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-8']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-8'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist or TypeError:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    try:
                        abundance = int(row['abundance-8'])
                    except (AttributeError, KeyError, ValueError):
                        continue
                    else:
                        if row['taxon-8'].lower() in ancylidae:
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

            def psi_f_9(csv_file):
                ab = 0
                sum_ab = 0
                sum_abcd = 0
                ancylidae = ['ancylus fluviatilis', 'ancylus sp.', 'ancylidae',
                             'ancylidae/acroloxidae', '"ancylidae" gen. sp.']
                families = {}
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-9']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-9'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist or TypeError:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    try:
                        abundance = int(row['abundance-9'])
                    except (AttributeError, KeyError, ValueError):
                        continue
                    else:
                        if row['taxon-9'].lower() in ancylidae:
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

            def psi_f_10(csv_file):
                ab = 0
                sum_ab = 0
                sum_abcd = 0
                ancylidae = ['ancylus fluviatilis', 'ancylus sp.', 'ancylidae',
                             'ancylidae/acroloxidae', '"ancylidae" gen. sp.']
                families = {}
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-10']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-10'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist or TypeError:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    try:
                        abundance = int(row['abundance-10'])
                    except (AttributeError, KeyError, ValueError):
                        continue
                    else:
                        if row['taxon-10'].lower() in ancylidae:
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


            def dehli_calc_1(csv_file):
                sum_dis = 0
                ntaxa = 0
                ancylidae = ['ancylus fluviatilis', 'ancylus sp.', 'ancylidae',
                             'ancylidae/acroloxidae', '"ancylidae" gen. sp.']
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-1']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-1'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    # else:

                    if row['taxon-1'].lower() in ancylidae:
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

            def dehli_calc_2(csv_file):
                sum_dis = 0
                ntaxa = 0
                ancylidae = ['ancylus fluviatilis', 'ancylus sp.', 'ancylidae',
                             'ancylidae/acroloxidae', '"ancylidae" gen. sp.']
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-2']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-2'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    # else:
                    if row['taxon-2'].lower() in ancylidae:
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

            def dehli_calc_3(csv_file):
                sum_dis = 0
                ntaxa = 0
                ancylidae = ['ancylus fluviatilis', 'ancylus sp.', 'ancylidae',
                             'ancylidae/acroloxidae', '"ancylidae" gen. sp.']
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-3']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-3'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    # else:
                    if row['taxon-3'].lower() in ancylidae:
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

            def dehli_calc_4(csv_file):
                sum_dis = 0
                ntaxa = 0
                ancylidae = ['ancylus fluviatilis', 'ancylus sp.', 'ancylidae',
                             'ancylidae/acroloxidae', '"ancylidae" gen. sp.']
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-4']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-4'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    # else:
                    if row['taxon-4'].lower() in ancylidae:
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

            def dehli_calc_5(csv_file):
                sum_dis = 0
                ntaxa = 0
                ancylidae = ['ancylus fluviatilis', 'ancylus sp.', 'ancylidae',
                             'ancylidae/acroloxidae', '"ancylidae" gen. sp.']
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-5']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-5'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    # else:
                    if row['taxon-5'].lower() in ancylidae:
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

            def dehli_calc_6(csv_file):
                sum_dis = 0
                ntaxa = 0
                ancylidae = ['ancylus fluviatilis', 'ancylus sp.', 'ancylidae',
                             'ancylidae/acroloxidae', '"ancylidae" gen. sp.']
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-6']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-6'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    # else:
                    if row['taxon-6'].lower() in ancylidae:
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

            def dehli_calc_7(csv_file):
                sum_dis = 0
                ntaxa = 0
                ancylidae = ['ancylus fluviatilis', 'ancylus sp.', 'ancylidae',
                             'ancylidae/acroloxidae', '"ancylidae" gen. sp.']
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-7']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-7'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    # else:
                    if row['taxon-7'].lower() in ancylidae:
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

            def dehli_calc_8(csv_file):
                sum_dis = 0
                ntaxa = 0
                ancylidae = ['ancylus fluviatilis', 'ancylus sp.', 'ancylidae',
                             'ancylidae/acroloxidae', '"ancylidae" gen. sp.']
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-8']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-8'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    # else:
                    if row['taxon-8'].lower() in ancylidae:
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

            def dehli_calc_9(csv_file):
                sum_dis = 0
                ntaxa = 0
                ancylidae = ['ancylus fluviatilis', 'ancylus sp.', 'ancylidae',
                             'ancylidae/acroloxidae', '"ancylidae" gen. sp.']
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-9']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-9'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    # else:
                    if row['taxon-9'].lower() in ancylidae:
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

            def dehli_calc_10(csv_file):
                sum_dis = 0
                ntaxa = 0
                ancylidae = ['ancylus fluviatilis', 'ancylus sp.', 'ancylidae',
                             'ancylidae/acroloxidae', '"ancylidae" gen. sp.']
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-10']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-10'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    # else:
                    if row['taxon-10'].lower() in ancylidae:
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


            def epsi_r_1(csv_file):
                ab = 0
                sum_sensitive = 0
                sum_all = 0
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-1']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-1'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    try:
                        abundance = int(row['abundance-1'])
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

            def epsi_r_2(csv_file):
                ab = 0
                sum_sensitive = 0
                sum_all = 0
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-2']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-2'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    try:
                        abundance = int(row['abundance-2'])
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

            def epsi_r_3(csv_file):
                ab = 0
                sum_sensitive = 0
                sum_all = 0
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-3']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-3'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    try:
                        abundance = int(row['abundance-3'])
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

            def epsi_r_4(csv_file):
                ab = 0
                sum_sensitive = 0
                sum_all = 0
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-4']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-4'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    try:
                        abundance = int(row['abundance-4'])
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

            def epsi_r_5(csv_file):
                ab = 0
                sum_sensitive = 0
                sum_all = 0
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-5']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-5'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    try:
                        abundance = int(row['abundance-5'])
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

            def epsi_r_6(csv_file):
                ab = 0
                sum_sensitive = 0
                sum_all = 0
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-6']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-6'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    try:
                        abundance = int(row['abundance-6'])
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

            def epsi_r_7(csv_file):
                ab = 0
                sum_sensitive = 0
                sum_all = 0
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-7']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-7'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    try:
                        abundance = int(row['abundance-7'])
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

            def epsi_r_8(csv_file):
                ab = 0
                sum_sensitive = 0
                sum_all = 0
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-8']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-8'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    try:
                        abundance = int(row['abundance-8'])
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

            def epsi_r_9(csv_file):
                ab = 0
                sum_sensitive = 0
                sum_all = 0
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-9']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-9'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    try:
                        abundance = int(row['abundance-9'])
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

            def epsi_r_10(csv_file):
                ab = 0
                sum_sensitive = 0
                sum_all = 0
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-10']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-10'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    try:
                        abundance = int(row['abundance-10'])
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


            def epsi_p_1(csv_file):
                ab = 0
                sum_sensitive = 0
                sum_all = 0
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-1']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-1'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    # else:
                    try:
                        abundance = int(row['abundance-1'])
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

            def epsi_p_2(csv_file):
                ab = 0
                sum_sensitive = 0
                sum_all = 0
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-2']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-2'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    # else:
                    try:
                        abundance = int(row['abundance-2'])
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
                elif ab ==0:
                    return None
                else:
                    epsi = round((sum_sensitive / sum_all) * 100, 2)
                    return epsi

            def epsi_p_3(csv_file):
                ab = 0
                sum_sensitive = 0
                sum_all = 0
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-3']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-3'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    # else:
                    try:
                        abundance = int(row['abundance-3'])
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
                elif ab ==0:
                    return None
                else:
                    epsi = round((sum_sensitive / sum_all) * 100, 2)
                    return epsi

            def epsi_p_4(csv_file):
                ab = 0
                sum_sensitive = 0
                sum_all = 0
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-4']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-4'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    # else:
                    try:
                        abundance = int(row['abundance-4'])
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
                elif ab ==0:
                    return None
                else:
                    epsi = round((sum_sensitive / sum_all) * 100, 2)
                    return epsi

            def epsi_p_5(csv_file):
                ab = 0
                sum_sensitive = 0
                sum_all = 0
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-5']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-5'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    # else:
                    try:
                        abundance = int(row['abundance-5'])
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
                elif ab ==0:
                    return None
                else:
                    epsi = round((sum_sensitive / sum_all) * 100, 2)
                    return epsi

            def epsi_p_6(csv_file):
                ab = 0
                sum_sensitive = 0
                sum_all = 0
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-6']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-6'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    # else:
                    try:
                        abundance = int(row['abundance-6'])
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
                elif ab ==0:
                    return None
                else:
                    epsi = round((sum_sensitive / sum_all) * 100, 2)
                    return epsi

            def epsi_p_7(csv_file):
                ab = 0
                sum_sensitive = 0
                sum_all = 0
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-7']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-7'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    # else:
                    try:
                        abundance = int(row['abundance-7'])
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
                elif ab ==0:
                    return None
                else:
                    epsi = round((sum_sensitive / sum_all) * 100, 2)
                    return epsi

            def epsi_p_8(csv_file):
                ab = 0
                sum_sensitive = 0
                sum_all = 0
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-8']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-8'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    # else:
                    try:
                        abundance = int(row['abundance-8'])
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
                elif ab ==0:
                    return None
                else:
                    epsi = round((sum_sensitive / sum_all) * 100, 2)
                    return epsi

            def epsi_p_9(csv_file):
                ab = 0
                sum_sensitive = 0
                sum_all = 0
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-9']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-9'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    # else:
                    try:
                        abundance = int(row['abundance-9'])
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
                elif ab ==0:
                    return None
                else:
                    epsi = round((sum_sensitive / sum_all) * 100, 2)
                    return epsi

            def epsi_p_10(csv_file):
                ab = 0
                sum_sensitive = 0
                sum_all = 0
                taxons = []
                for row in csv.DictReader(csv_file):
                    try:
                        if not Taxon.objects.get(taxon__iexact=row['taxon-10']):
                            continue
                    except ObjectDoesNotExist:
                        continue
                    else:
                    # try:
                        taxon = Taxon.objects.get(taxon__iexact=row['taxon-10'])
                        taxons.append(taxon)
                    # except ObjectDoesNotExist:
                    #     messages.error(request, 'Taxon not found in the database')
                    #     return redirect('index_calculator')
                    # else:
                    try:
                        abundance = int(row['abundance-10'])
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
                elif ab ==0:
                    return None
                else:
                    epsi = round((sum_sensitive / sum_all) * 100, 2)
                    return epsi


            def uk_bap_1(csv_file):
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
                    if row['taxon-1'].lower() in ukbap_species:
                        no_ukbap += 1

                if no_ukbap == 0:
                    return '0'
                else:
                    return no_ukbap

            def uk_bap_2(csv_file):
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
                    if row['taxon-2'].lower() in ukbap_species:
                        no_ukbap += 1

                if no_ukbap == 0:
                    return '0'
                else:
                    return no_ukbap

            def uk_bap_3(csv_file):
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
                    if row['taxon-3'].lower() in ukbap_species:
                        no_ukbap += 1

                if no_ukbap == 0:
                    return '0'
                else:
                    return no_ukbap

            def uk_bap_4(csv_file):
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
                    if row['taxon-4'].lower() in ukbap_species:
                        no_ukbap += 1

                if no_ukbap == 0:
                    return '0'
                else:
                    return no_ukbap

            def uk_bap_5(csv_file):
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
                    if row['taxon-5'].lower() in ukbap_species:
                        no_ukbap += 1

                if no_ukbap == 0:
                    return '0'
                else:
                    return no_ukbap

            def uk_bap_6(csv_file):
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
                    if row['taxon-6'].lower() in ukbap_species:
                        no_ukbap += 1

                if no_ukbap == 0:
                    return '0'
                else:
                    return no_ukbap

            def uk_bap_7(csv_file):
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
                    if row['taxon-7'].lower() in ukbap_species:
                        no_ukbap += 1

                if no_ukbap == 0:
                    return '0'
                else:
                    return no_ukbap

            def uk_bap_8(csv_file):
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
                    if row['taxon-8'].lower() in ukbap_species:
                        no_ukbap += 1

                if no_ukbap == 0:
                    return '0'
                else:
                    return no_ukbap

            def uk_bap_9(csv_file):
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
                    if row['taxon-9'].lower() in ukbap_species:
                        no_ukbap += 1

                if no_ukbap == 0:
                    return '0'
                else:
                    return no_ukbap

            def uk_bap_10(csv_file):
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
                    if row['taxon-10'].lower() in ukbap_species:
                        no_ukbap += 1

                if no_ukbap == 0:
                    return '0'
                else:
                    return no_ukbap


            def site_date_generator(csv_file):
                site_date = {}

                for row in csv.DictReader(csv_file):
                    if len(row['site-name-1']) == 0:
                        pass
                    else:
                        try:
                            site1 = row['site-name-1']
                            site_date['site1'] = site1
                        except:
                            pass
                    if len(row['sample-date-1']) == 0:
                        pass
                    else:
                        try:
                            date1 = row['sample-date-1']
                            site_date['date1'] = date1
                        except:
                            pass

                    if len(row['site-name-2']) == 0:
                        pass
                    else:
                        try:
                            site2 = row['site-name-2']
                            site_date['site2'] = site2
                        except:
                            pass
                    if len(row['sample-date-2']) == 0:
                        pass
                    else:
                        try:
                            date2 = row['sample-date-2']
                            site_date['date2'] = date2
                        except:
                            pass

                    if len(row['site-name-3']) == 0:
                        pass
                    else:
                        try:
                            site3 = row['site-name-3']
                            site_date['site3'] = site3
                        except:
                            pass
                    if len(row['sample-date-3']) == 0:
                        pass
                    else:
                        try:
                            date3 = row['sample-date-3']
                            site_date['date3'] = date3
                        except:
                            pass

                    if len(row['site-name-4']) == 0:
                        pass
                    else:
                        try:
                            site4 = row['site-name-4']
                            site_date['site4'] = site4
                        except:
                            pass
                    if len(row['sample-date-4']) == 0:
                        pass
                    else:
                        try:
                            date4 = row['sample-date-4']
                            site_date['date4'] = date4
                        except:
                            pass

                    if len(row['site-name-5']) == 0:
                        pass
                    else:
                        try:
                            site5 = row['site-name-5']
                            site_date['site5'] = site5
                        except:
                            pass
                    if len(row['sample-date-5']) == 0:
                        pass
                    else:
                        try:
                            date5 = row['sample-date-5']
                            site_date['date5'] = date5
                        except:
                            pass

                    if len(row['site-name-6']) == 0:
                        pass
                    else:
                        try:
                            site6 = row['site-name-6']
                            site_date['site6'] = site6
                        except:
                            pass
                    if len(row['sample-date-6']) == 0:
                        pass
                    else:
                        try:
                            date6 = row['sample-date-6']
                            site_date['date6'] = date6
                        except:
                            pass

                    if len(row['site-name-7']) == 0:
                        pass
                    else:
                        try:
                            site7 = row['site-name-7']
                            site_date['site7'] = site7
                        except:
                            pass
                    if len(row['sample-date-7']) == 0:
                        pass
                    else:
                        try:
                            date7 = row['sample-date-7']
                            site_date['date7'] = date7
                        except:
                            pass

                    if len(row['site-name-8']) == 0:
                        pass
                    else:
                        try:
                            site8 = row['site-name-8']
                            site_date['site8'] = site8
                        except:
                            pass
                    if len(row['sample-date-8']) == 0:
                        pass
                    else:
                        try:
                            date8 = row['sample-date-8']
                            site_date['date8'] = date8
                        except:
                            pass

                    if len(row['site-name-9']) == 0:
                        pass
                    else:
                        try:
                            site9 = row['site-name-9']
                            site_date['site9'] = site9
                        except:
                            pass
                    if len(row['sample-date-9']) == 0:
                        pass
                    else:
                        try:
                            date9 = row['sample-date-9']
                            site_date['date9'] = date9
                        except:
                            pass

                    if len(row['site-name-10']) == 0:
                        pass
                    else:
                        try:
                            site10 = row['site-name-10']
                            site_date['site10'] = site10
                        except:
                            pass
                    if len(row['sample-date-10']) == 0:
                        pass
                    else:
                        try:
                            date10 = row['sample-date-10']
                            site_date['date10'] = date10
                        except:
                            pass

                print(site_date)

                return site_date


            bmwp1 = bmwp_aspt_1(io_string_csv)
            io_string_csv.seek(0)

            whpt1 = whpt_aspt_1(io_string_csv)
            io_string_csv.seek(0)

            cci1 = cc_index_1(io_string_csv)
            io_string_csv.seek(0)

            lifesp1 = life_s_1(io_string_csv)
            io_string_csv.seek(0)

            lifef1 = life_f_1(io_string_csv)
            io_string_csv.seek(0)

            psis1 = psi_s_1(io_string_csv)
            io_string_csv.seek(0)

            psif1 = psi_f_1(io_string_csv)
            io_string_csv.seek(0)

            epsir1 = epsi_r_1(io_string_csv)
            io_string_csv.seek(0)

            epsip1 = epsi_p_1(io_string_csv)
            io_string_csv.seek(0)

            ukbap1 = uk_bap_1(io_string_csv)
            io_string_csv.seek(0)

            request.session['bmwp1'] = bmwp1
            request.session['whpt1'] = whpt1
            request.session['cci1'] = cci1
            request.session['lifesp1'] = lifesp1
            request.session['lifef1'] = lifef1
            request.session['psis1'] = psis1
            request.session['psif1'] = psif1
            request.session['epsir1'] = epsir1
            request.session['epsip1'] = epsip1
            request.session['ukbap1'] = ukbap1


            bmwp2 = bmwp_aspt_2(io_string_csv)
            io_string_csv.seek(0)

            whpt2 = whpt_aspt_2(io_string_csv)
            io_string_csv.seek(0)

            cci2 = cc_index_2(io_string_csv)
            io_string_csv.seek(0)

            lifesp2 = life_s_2(io_string_csv)
            io_string_csv.seek(0)

            lifef2 = life_f_2(io_string_csv)
            io_string_csv.seek(0)

            psis2 = psi_s_2(io_string_csv)
            io_string_csv.seek(0)

            psif2 = psi_f_2(io_string_csv)
            io_string_csv.seek(0)

            epsir2 = epsi_r_2(io_string_csv)
            io_string_csv.seek(0)

            epsip2 = epsi_p_2(io_string_csv)
            io_string_csv.seek(0)

            ukbap2 = uk_bap_2(io_string_csv)
            io_string_csv.seek(0)

            request.session['bmwp2'] = bmwp2
            request.session['whpt2'] = whpt2
            request.session['cci2'] = cci2
            request.session['lifesp2'] = lifesp2
            request.session['lifef2'] = lifef2
            request.session['psis2'] = psis2
            request.session['psif2'] = psif2
            request.session['epsir2'] = epsir2
            request.session['epsip2'] = epsip2
            request.session['ukbap2'] = ukbap2


            bmwp3 = bmwp_aspt_3(io_string_csv)
            io_string_csv.seek(0)

            whpt3 = whpt_aspt_3(io_string_csv)
            io_string_csv.seek(0)

            cci3 = cc_index_3(io_string_csv)
            io_string_csv.seek(0)

            lifesp3 = life_s_3(io_string_csv)
            io_string_csv.seek(0)

            lifef3 = life_f_3(io_string_csv)
            io_string_csv.seek(0)

            psis3 = psi_s_3(io_string_csv)
            io_string_csv.seek(0)

            psif3 = psi_f_3(io_string_csv)
            io_string_csv.seek(0)

            epsir3 = epsi_r_3(io_string_csv)
            io_string_csv.seek(0)

            epsip3 = epsi_p_3(io_string_csv)
            io_string_csv.seek(0)

            ukbap3 = uk_bap_3(io_string_csv)
            io_string_csv.seek(0)

            request.session['bmwp3'] = bmwp3
            request.session['whpt3'] = whpt3
            request.session['cci3'] = cci3
            request.session['lifesp3'] = lifesp3
            request.session['lifef3'] = lifef3
            request.session['psis3'] = psis3
            request.session['psif3'] = psif3
            request.session['epsir3'] = epsir3
            request.session['epsip3'] = epsip3
            request.session['ukbap3'] = ukbap3


            bmwp4 = bmwp_aspt_4(io_string_csv)
            io_string_csv.seek(0)

            whpt4 = whpt_aspt_4(io_string_csv)
            io_string_csv.seek(0)

            cci4 = cc_index_4(io_string_csv)
            io_string_csv.seek(0)

            lifesp4 = life_s_4(io_string_csv)
            io_string_csv.seek(0)

            lifef4 = life_f_4(io_string_csv)
            io_string_csv.seek(0)

            psis4 = psi_s_4(io_string_csv)
            io_string_csv.seek(0)

            psif4 = psi_f_4(io_string_csv)
            io_string_csv.seek(0)

            epsir4 = epsi_r_4(io_string_csv)
            io_string_csv.seek(0)

            epsip4 = epsi_p_4(io_string_csv)
            io_string_csv.seek(0)

            ukbap4 = uk_bap_4(io_string_csv)
            io_string_csv.seek(0)

            request.session['bmwp4'] = bmwp4
            request.session['whpt4'] = whpt4
            request.session['cci4'] = cci4
            request.session['lifesp4'] = lifesp4
            request.session['lifef4'] = lifef4
            request.session['psis4'] = psis4
            request.session['psif4'] = psif4
            request.session['epsir4'] = epsir4
            request.session['epsip4'] = epsip4
            request.session['ukbap4'] = ukbap4


            bmwp5 = bmwp_aspt_5(io_string_csv)
            io_string_csv.seek(0)

            whpt5 = whpt_aspt_5(io_string_csv)
            io_string_csv.seek(0)

            cci5 = cc_index_5(io_string_csv)
            io_string_csv.seek(0)

            lifesp5 = life_s_5(io_string_csv)
            io_string_csv.seek(0)

            lifef5 = life_f_5(io_string_csv)
            io_string_csv.seek(0)

            psis5 = psi_s_5(io_string_csv)
            io_string_csv.seek(0)

            psif5 = psi_f_5(io_string_csv)
            io_string_csv.seek(0)

            epsir5 = epsi_r_5(io_string_csv)
            io_string_csv.seek(0)

            epsip5 = epsi_p_5(io_string_csv)
            io_string_csv.seek(0)

            ukbap5 = uk_bap_5(io_string_csv)
            io_string_csv.seek(0)

            request.session['bmwp5'] = bmwp5
            request.session['whpt5'] = whpt5
            request.session['cci5'] = cci5
            request.session['lifesp5'] = lifesp5
            request.session['lifef5'] = lifef5
            request.session['psis5'] = psis5
            request.session['psif5'] = psif5
            request.session['epsir5'] = epsir5
            request.session['epsip5'] = epsip5
            request.session['ukbap5'] = ukbap5


            bmwp6 = bmwp_aspt_6(io_string_csv)
            io_string_csv.seek(0)

            whpt6 = whpt_aspt_6(io_string_csv)
            io_string_csv.seek(0)

            cci6 = cc_index_6(io_string_csv)
            io_string_csv.seek(0)

            lifesp6 = life_s_6(io_string_csv)
            io_string_csv.seek(0)

            lifef6 = life_f_6(io_string_csv)
            io_string_csv.seek(0)

            psis6 = psi_s_6(io_string_csv)
            io_string_csv.seek(0)

            psif6 = psi_f_6(io_string_csv)
            io_string_csv.seek(0)

            epsir6 = epsi_r_6(io_string_csv)
            io_string_csv.seek(0)

            epsip6 = epsi_p_6(io_string_csv)
            io_string_csv.seek(0)

            ukbap6 = uk_bap_6(io_string_csv)
            io_string_csv.seek(0)

            request.session['bmwp6'] = bmwp6
            request.session['whpt6'] = whpt6
            request.session['cci6'] = cci6
            request.session['lifesp6'] = lifesp6
            request.session['lifef6'] = lifef6
            request.session['psis6'] = psis6
            request.session['psif6'] = psif6
            request.session['epsir6'] = epsir6
            request.session['epsip6'] = epsip6
            request.session['ukbap6'] = ukbap6


            bmwp7 = bmwp_aspt_7(io_string_csv)
            io_string_csv.seek(0)

            whpt7 = whpt_aspt_7(io_string_csv)
            io_string_csv.seek(0)

            cci7 = cc_index_7(io_string_csv)
            io_string_csv.seek(0)

            lifesp7 = life_s_7(io_string_csv)
            io_string_csv.seek(0)

            lifef7 = life_f_7(io_string_csv)
            io_string_csv.seek(0)

            psis7 = psi_s_7(io_string_csv)
            io_string_csv.seek(0)

            psif7 = psi_f_7(io_string_csv)
            io_string_csv.seek(0)

            epsir7 = epsi_r_7(io_string_csv)
            io_string_csv.seek(0)

            epsip7 = epsi_p_7(io_string_csv)
            io_string_csv.seek(0)

            ukbap7 = uk_bap_7(io_string_csv)
            io_string_csv.seek(0)

            request.session['bmwp7'] = bmwp7
            request.session['whpt7'] = whpt7
            request.session['cci7'] = cci7
            request.session['lifesp7'] = lifesp7
            request.session['lifef7'] = lifef7
            request.session['psis7'] = psis7
            request.session['psif7'] = psif7
            request.session['epsir7'] = epsir7
            request.session['epsip7'] = epsip7
            request.session['ukbap7'] = ukbap7


            bmwp8 = bmwp_aspt_8(io_string_csv)
            io_string_csv.seek(0)

            whpt8 = whpt_aspt_8(io_string_csv)
            io_string_csv.seek(0)

            cci8 = cc_index_8(io_string_csv)
            io_string_csv.seek(0)

            lifesp8 = life_s_8(io_string_csv)
            io_string_csv.seek(0)

            lifef8 = life_f_8(io_string_csv)
            io_string_csv.seek(0)

            psis8 = psi_s_8(io_string_csv)
            io_string_csv.seek(0)

            psif8 = psi_f_8(io_string_csv)
            io_string_csv.seek(0)

            epsir8 = epsi_r_8(io_string_csv)
            io_string_csv.seek(0)

            epsip8 = epsi_p_8(io_string_csv)
            io_string_csv.seek(0)

            ukbap8 = uk_bap_8(io_string_csv)
            io_string_csv.seek(0)

            request.session['bmwp8'] = bmwp8
            request.session['whpt8'] = whpt8
            request.session['cci8'] = cci8
            request.session['lifesp8'] = lifesp8
            request.session['lifef8'] = lifef8
            request.session['psis8'] = psis8
            request.session['psif8'] = psif8
            request.session['epsir8'] = epsir8
            request.session['epsip8'] = epsip8
            request.session['ukbap8'] = ukbap8


            bmwp9 = bmwp_aspt_9(io_string_csv)
            io_string_csv.seek(0)

            whpt9 = whpt_aspt_9(io_string_csv)
            io_string_csv.seek(0)

            cci9 = cc_index_9(io_string_csv)
            io_string_csv.seek(0)

            lifesp9 = life_s_9(io_string_csv)
            io_string_csv.seek(0)

            lifef9 = life_f_9(io_string_csv)
            io_string_csv.seek(0)

            psis9 = psi_s_9(io_string_csv)
            io_string_csv.seek(0)

            psif9 = psi_f_9(io_string_csv)
            io_string_csv.seek(0)

            epsir9 = epsi_r_9(io_string_csv)
            io_string_csv.seek(0)

            epsip9 = epsi_p_9(io_string_csv)
            io_string_csv.seek(0)

            ukbap9 = uk_bap_9(io_string_csv)
            io_string_csv.seek(0)

            request.session['bmwp9'] = bmwp9
            request.session['whpt9'] = whpt9
            request.session['cci9'] = cci9
            request.session['lifesp9'] = lifesp9
            request.session['lifef9'] = lifef9
            request.session['psis9'] = psis9
            request.session['psif9'] = psif9
            request.session['epsir9'] = epsir9
            request.session['epsip9'] = epsip9
            request.session['ukbap9'] = ukbap9


            bmwp10 = bmwp_aspt_10(io_string_csv)
            io_string_csv.seek(0)

            whpt10 = whpt_aspt_10(io_string_csv)
            io_string_csv.seek(0)

            cci10 = cc_index_10(io_string_csv)
            io_string_csv.seek(0)

            lifesp10 = life_s_10(io_string_csv)
            io_string_csv.seek(0)

            lifef10 = life_f_10(io_string_csv)
            io_string_csv.seek(0)

            psis10 = psi_s_10(io_string_csv)
            io_string_csv.seek(0)

            psif10 = psi_f_10(io_string_csv)
            io_string_csv.seek(0)

            epsir10 = epsi_r_10(io_string_csv)
            io_string_csv.seek(0)

            epsip10 = epsi_p_10(io_string_csv)
            io_string_csv.seek(0)

            ukbap10 = uk_bap_10(io_string_csv)
            io_string_csv.seek(0)

            request.session['bmwp10'] = bmwp10
            request.session['whpt10'] = whpt10
            request.session['cci10'] = cci10
            request.session['lifesp10'] = lifesp10
            request.session['lifef10'] = lifef10
            request.session['psis10'] = psis10
            request.session['psif10'] = psif10
            request.session['epsir10'] = epsir10
            request.session['epsip10'] = epsip10
            request.session['ukbap10'] = ukbap10


            site_date = site_date_generator(io_string_csv)
            io_string_csv.seek(0)

            request.session['site_date'] = site_date

            try:
                dehli1 = dehli_calc_1(io_string_dehli)
                io_string_dehli.seek(0)

                dehli2 = dehli_calc_2(io_string_dehli)
                io_string_dehli.seek(0)

                dehli3 = dehli_calc_3(io_string_dehli)
                io_string_dehli.seek(0)

                dehli4 = dehli_calc_4(io_string_dehli)
                io_string_dehli.seek(0)

                dehli5 = dehli_calc_5(io_string_dehli)
                io_string_dehli.seek(0)

                dehli6 = dehli_calc_6(io_string_dehli)
                io_string_dehli.seek(0)

                dehli7 = dehli_calc_7(io_string_dehli)
                io_string_dehli.seek(0)

                dehli8 = dehli_calc_8(io_string_dehli)
                io_string_dehli.seek(0)

                dehli9 = dehli_calc_9(io_string_dehli)
                io_string_dehli.seek(0)

                dehli10 = dehli_calc_10(io_string_dehli)
                io_string_dehli.seek(0)

                request.session['dehli1'] = dehli1
                request.session['dehli2'] = dehli2
                request.session['dehli3'] = dehli3
                request.session['dehli4'] = dehli4
                request.session['dehli5'] = dehli5
                request.session['dehli6'] = dehli6
                request.session['dehli7'] = dehli7
                request.session['dehli8'] = dehli8
                request.session['dehli9'] = dehli9
                request.session['dehli10'] = dehli10

            except:
                pass

            return redirect('index_calculator')
