from django.shortcuts import render, redirect
from urllib.parse import quote

from .forms import CustomerInquiryForm


def customer_form(request):

    if request.method == "POST":

        form = CustomerInquiryForm(request.POST)

        if form.is_valid():

            inquiry = form.save()

            message = f"""
New ASTRA BUILDTECH Inquiry

Name: {inquiry.name}

Mobile: {inquiry.mobile}

Location: {inquiry.location}

Service: {inquiry.service}

Message: {inquiry.message}
"""

            whatsapp_url = (
                "https://wa.me/919356961833?text="
                + quote(message)
            )

            return render(
    request,
    'success.html',
    {'whatsapp_url': whatsapp_url}
)


    else:

        form = CustomerInquiryForm()


    return render(
        request,
        'customer_form.html',
        {'form': form}
    )
