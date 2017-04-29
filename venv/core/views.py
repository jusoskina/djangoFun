from django.shortcuts import render, HttpResponse, redirect

from core.models import UserSetting, BuyerAccount

def index(request):
    context = dict()

    if request.method == 'GET':
        context['subit'] = False
        return render(request, 'index.html', context)

    elif request.method == 'POST':
        buyer_name = request.POST['buyer']
        account_id = request.POST['account_id']
        context['submit'] = True

        buyer_account = BuyerAccount.objects.create(
            name=buyer_name,
            account_id=account_id
        )

        context['buyer_account'] = buyer_account
        return render(request, 'index.html', context)

def buyers(request):
    context = dict()
    buyer_accounts = BuyerAccount.objects.all()
    context['buyer_accounts'] = buyer_accounts
    return render(request, 'buyers.html', context)

def delete_buyer(request, buyer_id):
    context = dict()
    buyer_accounts = BuyerAccount.objects.get(id=buyer_id)
    context['buyer_account'] = buyer_accounts
    context['buyer_account'].delete()
    #context['buyer_accounts'] = BuyerAccount.objects.all()
    return redirect('/buyers/')

def postgresql_example(request):
    conn = psycopg2.connect("connect_timeout=20, dbname='" + settings.REDSHIFT_DB + "' port='" + settings.REDSHIFT_PORT + "' user='" + settings.REDSHIFT_USER + "' host='" + settings.REDSHIFT_HOST + "' password='" + settings.REDSHIFT_PASSWORD + "'")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM fulcrum_demand WHERE demand_date > '06/08/2016 21:00:00' and countrylanguage = 'English - United States';")

    for row in cursor.fetchall():
        SupplyData.objects.create()
        #Google charts to display
        # check out marketplaceMonitor
        # check out D3js

    cursor.close()
    conn.close()
