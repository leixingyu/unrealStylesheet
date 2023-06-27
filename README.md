# Unreal Stylesheet
 A Qt stylesheet designed to make your tools look native in Unreal Engine 5  

<img src="https://i.imgur.com/y7UP7k3.jpg" alt="main" width="100%"/>  

## Installation
PIP install the [latest release](https://pypi.org/project/unreal-qt-stylesheet/) from PYPi (recommended):
```
python -m pip install unreal-qt-stylesheet
```
or install from the repo:
```
python -m pip install git+https://github.com/hannesdelbeke/unrealStylesheet
```

## Using the stylesheet

Simply import `unreal_qt_stylesheet` and call `setup()`:  

```python
# ensure you have a Qt application:
# app = QtWidgets.QApplication(sys.argv)

import unreal_qt_stylesheet
unreal_qt_stylesheet.setup()

# show your qt widgets
# window = YourTool()
# window.show()
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

You can modify the `.qss` style sheet directly,  
or you can modify on top of the _CSS_ preprocessor `.scss` file.  
Once finished, re-compile the `.qss`:   
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


## References
- Qt documentation: 
    - [stylesheets examples](https://doc.qt.io/qt-5/stylesheet-examples.html)
    - [stylesheets reference](https://doc.qt.io/qt-5/stylesheet-reference.html)
- Github repo: [Qt-Material](https://github.com/UN-GCPDS/qt-material)
- Unreal has a different UI framework (Slate), future [read](https://minimaleffort.tech/qt-to-slate-transition-guide/) on comparing Qt to Slate
- An example of this stylesheet in action: [unrealScriptEditor](https://github.com/leixingyu/unrealScriptEditor)
