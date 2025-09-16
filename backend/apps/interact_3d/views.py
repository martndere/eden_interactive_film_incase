from django.shortcuts import render
from django.conf import settings

def model_viewer_view(request):
    """
    This view prepares the context for and renders the 3D model viewer.
    """
    # --- Step 1: Define the model to display ---
    # Place your .glb file in: /media/models/
    # Then, change the filename here to match yours.
    model_filename = "your_model.glb"
    model_url = f"{settings.MEDIA_URL}models/{model_filename}"

    # --- Step 2: Define the scene configuration ---
    # This data is passed to your Three.js script.
    scene_config = {
        "backgroundColor": 0x1a1a1a,
        "cameraFov": 75,
    }

    context = {
        'model_url': model_url,
        'scene_config': scene_config,
    }
    
    # --- Step 3: Render the template with the context ---
    return render(request, 'interact_3d/viewer.html', context)
