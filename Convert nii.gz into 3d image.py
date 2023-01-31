import itk
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersGeneral import vtkDiscreteMarchingCubes
from vtkmodules.vtkRenderingCore import vtkActor, vtkPolyDataMapper, vtkRenderer, vtkRenderWindow, vtkRenderWindowInteractor

def show_3d_nifti_image(nifti_file_name):

    itk_img = itk.imread(filename=nifti_file_name)
    vtk_img = itk.vtk_image_from_image(l_image=itk_img)
    contour = vtkDiscreteMarchingCubes()
    contour.SetInputData(vtk_img)

    colors = vtkNamedColors()

    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(contour.GetOutputPort())

    actor = vtkActor()
    actor.SetMapper(mapper)

    renderer = vtkRenderer()
    renderer.AddActor(actor)
    renderer.SetBackground(colors.GetColor3d("Black"))

    renderWindow = vtkRenderWindow()
    renderWindow.AddRenderer(renderer)

    renderWindowInteractor = vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)
    renderWindowInteractor.Initialize()
    renderWindowInteractor.Start()

if __name__ == '__main__':
     show_3d_nifti_image("C:/Desktop/mri_vessel001.nii.gz")