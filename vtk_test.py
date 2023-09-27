#!/usr/bin/env/python

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonCore import *
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
    vtkRenderer,
    vtkTextProperty
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
    axes.SetTotalLength(0.1, 0.1, 0.1)

    font_file_path = "C:/Users/think/Desktop/AlibabaPuHuiTi-2-55-Regular.ttf"  # 替换为你的字体文件路径
    text_property = vtkTextProperty()
    text_property.SetFontFamily(VTK_FONT_FILE)
    text_property.SetFontFile(font_file_path)
    text_property.SetFontSize(20)  # 设置文字大小
    text_property.SetBold(True)   # 设置为粗体
    text_property.SetItalic(False)  # 设置为斜体
    text_property.SetColor(1.0, 0.0, 0.0)  # 设置文字颜色
    axes.GetXAxisCaptionActor2D().SetCaptionTextProperty(text_property)
    axes.SetXAxisLabelText("Yang Luo最牛逼")
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