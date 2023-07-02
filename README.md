# Unreal Stylesheet [![PyPI](https://img.shields.io/pypi/v/unreal_stylesheet?color=blue)](https://pypi.org/project/unreal-stylesheet/)

 A Qt stylesheet designed to make your tools look native in Unreal Engine 5  

Quickstart sample code:
```python
import unreal_stylesheet

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    # style your QApp, requires a QApplication instance
    unreal_stylesheet.setup()  # <== Just 1 line of code to make the magic happen

    # create & show your Qt widget
    window = TestWindow()
    window.show()
    sys.exit(app.exec_())                   
```

<img src="https://i.imgur.com/y7UP7k3.jpg" alt="main" width="100%"/>  

## Installation
PIP install the [latest release](https://pypi.org/project/unreal-stylesheet/) from PYPi (recommended):
```
python -m pip install unreal-stylesheet
```
or install from the repo:
```
python -m pip install git+https://github.com/leixingyu/unrealStylesheet
```

## Comparison

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

## Contribute

Feel free to make a PR or issue if you find a bug, or want to request a feature.  
Some guidelines to modify this stylesheet:

### Modifying the style sheet

1. Modify the _CSS_ preprocessor `.scss` file
2. Re-compile the `.qss`:   
```commandline
qtsass ue.scss -o ue.qss
```

⚠️ If you modify the `.qss` style sheet directly, your changes will be lost when the `.qss` is re-compiled in the future  

> Documentation about .scss can be found: [Sass Official website](https://sass-lang.com/guide)  
> You'll also need to install a Qt specific Sass: [qt-sass](https://github.com/spyder-ide/qtsass)  

### Modifying icons

The icons are handled with Qt's resource system (see the [docs](https://doc.qt.io/qt-5/resources.html)) (which is dropped in qt6)

1. Modify the `.qrc` file
2. Re-compile the `.rcc` :
```commandline
rcc -binary icons.qrc -o icons.rcc
```

## References
- Qt documentation: 
    - [stylesheets examples](https://doc.qt.io/qt-5/stylesheet-examples.html)
    - [stylesheets reference](https://doc.qt.io/qt-5/stylesheet-reference.html)
- Github repo: [Qt-Material](https://github.com/UN-GCPDS/qt-material)
- Unreal has a different UI framework (Slate), future [read](https://minimaleffort.tech/qt-to-slate-transition-guide/) on comparing Qt to Slate
- An example of this stylesheet in action: [unrealScriptEditor](https://github.com/leixingyu/unrealScriptEditor)
