from django.contrib import messages
from django.shortcuts import render

from procesos.models import Proceso
from procesos.forms import ProcesoForm

def create_procesos(request):
    if request.method == "POST":
        proceso_form = ProcesoForm(request.POST)
        print("-------------------------------------+++++++++++++++++")
        if proceso_form.is_valid():
            data = proceso_form.cleaned_data
            actual_objects = Proceso.objects.filter(
                juzgado=data["juzgado"], radicado=data["radicado"]
            ).count()
            print("actual_objects", actual_objects)
            if actual_objects:
                messages.error(
                    request,
                    f"El proceso {data['juzgado']} - {data['radicado']} ya está creado",
                )
            else:
                proceso = Proceso(juzgado=data["juzgado"], radicado=data["radicado"])
                proceso.save()
                messages.success(
                    request,
                    f"despacho  {data['juzgado']} - {data['radicado']} creado exitosamente!",
                )

            return render(
                request=request,
                context={"procesos": Proceso.objects.all()},
                template_name="procesos/proceso_list.html",
            )

    proceso_form = ProcesoForm(request.POST)
    context_dict = {"form": proceso_form}
    return render(
        request=request,
        context=context_dict,
        template_name="procesos/proceso_form.html",
    )


def procesos(request):
    return render(
        request=request,
        context={"procesos": Proceso.objects.all()},
        template_name="procesos/proceso_list.html",
    )