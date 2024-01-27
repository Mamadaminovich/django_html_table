from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    context = {
        "table": [
            [261, "Alfred Alan", "aalan@gmail.com", "Stocks", "ok"],
            [262, "Maria Sanchez", "aalan@gmail.com", "Stocks", "ok"],
            [263, "Alfred Alan", "aalan@gmail.com", "Stocks", "ok"],
            [264, "Maria Sanchez", "aalan@gmail.com", "Stocks", "ok"],
            [266, "Alfred Alan", "aalan@gmail.com", "Stocks", "ok"],
            [268, "Maria Sanchez", "aalan@gmail.com", "Stocks", "ok"],
            [267, "Alfred Alan", "aalan@gmail.com", "Stocks", "ok"],
        ]
    }

    return render(request=request, template_name='index.html', context={"table": context["table"]})