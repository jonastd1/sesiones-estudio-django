from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import SesionEstudio
from .forms import SesionForm


@login_required
def sesion_lista(request):
    sesiones = SesionEstudio.objects.filter(usuario=request.user)

    materia = request.GET.get('materia', '').strip()
    estado = request.GET.get('estado', '')
    desde = request.GET.get('desde', '')

    if materia:
        sesiones = sesiones.filter(materia__icontains=materia)
    if estado == '1':
        sesiones = sesiones.filter(completada=True)
    elif estado == '0':
        sesiones = sesiones.filter(completada=False)
    if desde:
        sesiones = sesiones.filter(fecha__gte=desde)

    page_obj = Paginator(sesiones, 5).get_page(request.GET.get('page'))

    params = request.GET.copy()
    params.pop('page', None)

    return render(request, 'sesion_lista.html', {
        'page_obj': page_obj,
        'querystring': params.urlencode(),
        'materia': materia,
        'estado': estado,
        'desde': desde,
    })


@login_required
def sesion_detalle(request, pk):
    sesion = get_object_or_404(SesionEstudio, pk=pk, usuario=request.user)
    return render(request, 'sesion_detalle.html', {'sesion': sesion})


@login_required
def sesion_crear(request):
    form = SesionForm(request.POST or None)
    if form.is_valid():
        sesion = form.save(commit=False)
        sesion.usuario = request.user
        sesion.save()
        return redirect('sesion_lista')
    return render(request, 'sesion_form.html', {'form': form, 'titulo': 'Nueva sesión'})


@login_required
def sesion_editar(request, pk):
    sesion = get_object_or_404(SesionEstudio, pk=pk, usuario=request.user)
    form = SesionForm(request.POST or None, instance=sesion)
    if form.is_valid():
        form.save()
        return redirect('sesion_detalle', pk=sesion.pk)
    return render(request, 'sesion_form.html', {'form': form, 'titulo': 'Editar sesión'})


@login_required
def sesion_eliminar(request, pk):
    sesion = get_object_or_404(SesionEstudio, pk=pk, usuario=request.user)
    if request.method == 'POST':
        sesion.delete()
        return redirect('sesion_lista')
    return render(request, 'sesion_eliminar.html', {'sesion': sesion})