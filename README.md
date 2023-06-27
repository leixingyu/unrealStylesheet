<div align="center">
<h1 align="center">Unreal Style Sheet</h1>

  <p align="center">
    A Qt style sheet designed to make your tools look native in Unreal Engine 5
  </p>
</div>

## About The Project

<br>

<div align="center">
<img src="https://i.imgur.com/y7UP7k3.jpg" alt="main" width="100%"/>
</div>

<br>

This side project is my personal attempt to make Qt application feels 
more natural in Unreal Engine 5.
The style sheet covers some of the most common used widgets, and tries to
match the Unreal native UI as close as possible.

If you feel there's anything missing, feel free to submit an issue or a PR.


## Getting Started

### Using the style sheet
simply import `unreal_qt_stylesheet` and call `setup()`:
```python
# ensure you have a Qt application:
# app = QtWidgets.QApplication(sys.argv)

import unreal_qt_stylesheet
unreal_qt_stylesheet.setup()

# show your qt widgets
# window = YourTool()
# window.show()
```

### Comparison

The following `.ui` files for testing can be found inside the `/ui` folder.

|default (editor.ui)| ue.qss|
|---|---|
|![](https://i.imgur.com/EX5naMy.png)| ![](https://i.imgur.com/M8CU4cN.jpg)|

|default (tree.ui)|ue.qss |
|---|---|
|![](https://i.imgur.com/Xk8XYlQ.png)|![](https://i.imgur.com/DcQQwak.jpg) |

|default (progress.ui)| ue.qss|
|---|---|
|![](https://i.imgur.com/6yMuCKD.png)| ![](https://i.imgur.com/NyskX8m.jpg)|



### Modifying the style sheet

You can modify the `.qss` style sheet directly, 

or you can modify on top of the
_CSS_ preprocessor `.scss` file.
Once finished, re-compile the `.qss` as follows:

```commandline
qtsass ue.scss -o ue.qss
```

> Documentation about .scss can be found: [Sass Official website](https://sass-lang.com/guide)
>
> You'll also need to install a Qt specific Sass: [qt-sass](https://github.com/spyder-ide/qtsass)

### Modifying icons

The icons are handled with Qt's resource system (to learn more, visit [here](https://doc.qt.io/qt-5/resources.html))

You can modify the `.qrc` file and re-compile the `.rcc` as follows:

```commandline
rcc -binary icons.qrc -o icons.rcc
```


## Reference

[Qt Documentation: Qt Style Sheets Examples](https://doc.qt.io/qt-5/stylesheet-examples.html)

[Qt Documentation: Qt Style Sheets Reference](https://doc.qt.io/qt-5/stylesheet-reference.html)

[Github: Qt-Material](https://github.com/UN-GCPDS/qt-material)

> Unreal has a different UI framework (Slate), future [read](https://minimaleffort.tech/qt-to-slate-transition-guide/) on comparing Qt to Slate 
