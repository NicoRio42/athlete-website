from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse

from .models import HeadBanner, HeadText, Article, SponsorBanner, Sponsor
from .forms import ContactForm

def index(request):
    head_banners = HeadBanner.objects.order_by('pk')
    if head_banners:
        head_banner = head_banners[0]
    else:
        head_banner = None

    head_texts = HeadText.objects.order_by('pk')
    if head_texts:
        head_text = head_texts[0]
    else:
        head_text = None

    article_list = Article.objects.order_by('pk')

    sponsor_banners = HeadText.objects.order_by('pk')
    if sponsor_banners:
        sponsor_banner = sponsor_banners[0]
    else:
        sponsor_banner = None

    sponsor_list = Sponsor.objects.order_by('pk')

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            name = form.cleaned_data['name']
            email_adress = form.cleaned_data['email_adress']
            message = form.cleaned_data['message']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['nicolas.rio42@gmail.com']
            if cc_myself:
                recipients.append(email_adress)

            print('email envoyé !')
            # send_mail(("Message from athlete website from " + name), message, email_adress, recipients)
            return HttpResponseRedirect('thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()
    
    context = {
        'head_banner': head_banner,
        'head_text': head_text,
        'article_list': article_list,
        'sponsor_banner': sponsor_banner,
        'sponsor_list': sponsor_list,
        'form': form,
    }

    return render(request, 'athlete/index.html', context)

def article(request, article_slug):
    article = get_object_or_404(Article, slug=article_slug)

    article_list = Article.objects.order_by('pk')
    sponsor_banner = SponsorBanner.objects.order_by('pk')[0]
    sponsor_list = Sponsor.objects.order_by('pk')

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            name = form.cleaned_data['name']
            email_adress = form.cleaned_data['email_adress']
            message = form.cleaned_data['message']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['nicolas.rio42@gmail.com']
            if cc_myself:
                recipients.append(email_adress)

            print('email envoyé !')
            # send_mail(("Message from athlete website from " + name), message, email_adress, recipients)
            return HttpResponseRedirect('thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()
    
    context = {
        'article_list': article_list,
        'sponsor_banner': sponsor_banner,
        'sponsor_list': sponsor_list,
        'article': article,
        'form': form,
    }

    return render(request, 'athlete/article.html', context)

def thanks(request):
    return HttpResponse('Thank you!')