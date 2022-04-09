from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from .models import Property
from .forms import ImageForm


class ListProperties(ListView):
    model = Property
    template_name = 'list_properties.html'

class UpdateProperty(UpdateView):
    pass

class DeleteProperty(DeleteView):
    pass

class CreateProperty(CreateView):
    pass

class DetailProperty(DetailView):
    pass


def image_upload_view(request, pk):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            related_property = Property.objects.get(pk=pk)
            form.save()
            # Get the current instance object to add the property and
            #  display the image in the template
            img_obj = form.instance
            img_obj.property = related_property
            img_obj.save()
            return render(request, 'upload_image.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'upload_image.html', {'form': form})