#!/usr/bin/env/python

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonTransforms import vtkTransform
from vtkmodules.vtkFiltersSources import vtkSphereSource, vtkPlaneSource
from vtkmodules.vtkRenderingAnnotation import vtkAxesActor
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleTrackballCamera
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)


def main():
    colors = vtkNamedColors()

    # create a Sphere
    sphereSource = vtkSphereSource()
    sphereSource.SetCenter(0.0, 0.0, 0.0)
    sphereSource.SetRadius(0.5)

    # create a mapper
    sphereMapper = vtkPolyDataMapper()
    sphereMapper.SetInputConnection(sphereSource.GetOutputPort())

    # create an actor
    sphereActor = vtkActor()
    sphereActor.SetMapper(sphereMapper)

    # a renderer and render window
    renderer = vtkRenderer()
    renderWindow = vtkRenderWindow()
    renderWindow.SetWindowName('Axes')
    renderWindow.AddRenderer(renderer)

    # an interactor
    renderWindowInteractor = vtkRenderWindowInteractor()
    renderWindowInteractor.SetInteractorStyle(vtkInteractorStyleTrackballCamera())
    renderWindowInteractor.SetRenderWindow(renderWindow)

    # add the actors to the scene
    renderer.AddActor(sphereActor)
    renderer.SetBackground(colors.GetColor3d('SlateGray'))

    transform = vtkTransform()
    transform.Translate(1.0, 0.0, 0.0)

    axes = vtkAxesActor()
    #  The axes are positioned with a user transform
    axes.SetUserTransform(transform)

    # properties of the axes labels can be set as follows
    # this sets the x axis label to red
    # axes.GetXAxisCaptionActor2D().GetCaptionTextProperty().SetColor(colors.GetColor3d('Red'));

    # the actual text of the axis label can be changed:
    # axes->SetXAxisLabelText('test');

    renderer.AddActor(axes)


    planeSource= vtkPlaneSource()
    planeSource.SetCenter(0.0, 0.0, 0.0)
    planeSource.SetNormal(0.0, 0.0, 1.0)
    planeSource.SetXResolution(10)
    planeSource.SetYResolution(10)
    planeSource.SetPoint1(5.0, -5.0, 0.0)
    planeSource.SetPoint2(-5.0, 5.0, 0.0)
    planeSource.SetOrigin(-5.0, -5.0, 0.0)

    print(planeSource.GetPoint1())
    print(planeSource.GetPoint2())
    print(planeSource.GetOrigin())
    planeSource.Update()
    
    plane = planeSource.GetOutput()
    planeMapper = vtkPolyDataMapper()
    planeMapper.SetInputData(plane)

    planeActor = vtkActor()
    planeActor.SetMapper(planeMapper)
    planeActor.GetProperty().SetRepresentationToWireframe()

    renderer.AddActor(planeActor)
    

    renderer.GetActiveCamera().Azimuth(50)
    renderer.GetActiveCamera().Elevation(-30)

    renderer.ResetCamera()
    renderWindow.SetWindowName('Axes')
    renderWindow.Render()

    # begin mouse interaction
    renderWindowInteractor.Start()


if __name__ == '__main__':
    main()