### 安装 android studio 

下载android studio: https://developer.android.com/studio

设置android SDK :
/Users/tech/Library/Android/sdk

配置环境变量：```sudo vi ~/.bash_profile```

```shell
ANDROID_HOME=/Users/tech/Library/Android/sdk
PATH=${PATH}:${ANDROID_HOME}/platform-tools
PATH=${PATH}:${ANDROID_HOME}/tools
```
最后，使变量生效：```source ~/.bash_profile```

### 安装appium 

1、安装appium 

``` shell
> brew install node      # get node.js
> npm install -g appium  # get appium
```

2、安装appium-doctor

```shell
> npm install appium-doctor
```
检查环境：

```shell
appium-doctor
info AppiumDoctor Appium Doctor v.1.11.0
info AppiumDoctor ### Diagnostic for necessary dependencies starting ###
info AppiumDoctor  ✔ The Node.js binary was found at: /usr/local/bin/node
info AppiumDoctor  ✔ Node version is 10.15.1
WARN AppiumDoctor  ✖ Xcode is NOT installed!
info AppiumDoctor  ✔ Xcode Command Line Tools are installed in: /Library/Developer/CommandLineTools
info AppiumDoctor  ✔ DevToolsSecurity is enabled.
info AppiumDoctor  ✔ The Authorization DB is set up properly.
WARN AppiumDoctor  ✖ Carthage was NOT found!
info AppiumDoctor  ✔ HOME is set to: /Users/tech
info AppiumDoctor  ✔ ANDROID_HOME is set to: /Users/tech/Library/Android/sdk
info AppiumDoctor  ✔ JAVA_HOME is set to: /Library/Java/JavaVirtualMachines/jdk-9.0.1.jdk/Contents/Home
info AppiumDoctor  ✔ adb exists at: /Users/tech/Library/Android/sdk/platform-tools/adb
info AppiumDoctor  ✔ android exists at: /Users/tech/Library/Android/sdk/tools/android
info AppiumDoctor  ✔ emulator exists at: /Users/tech/Library/Android/sdk/tools/emulator
info AppiumDoctor  ✔ Bin directory of $JAVA_HOME is set
...
```

### appium AI 插件

GtiHub地址:https://github.com/testdotai/appium-classifier-plugin

使用Appium 1.9.2-beta版以上。另外，一定要使用 XCUITest 驱动程序(用于iOS)或UiAutomator2或Espresso驱动程序(用于
Android)。较老的iOS和Android驱动程序不支持所需的Appium在任何情况下，都不推荐使用。

### 操作系统设置：

首先，需要一些系统依赖项来处理图像。

* macOS

```
brew install pkg-config cairo pango libpng jpeg giflib
```

* Linux
```
sudo apt-get install pkg-config libcairo2-dev libpango* libpng-dev libjpeg-dev giflib*
```
* Windows

暂不支持

如果遇到问题，您可能必须单独安装每个包。


### Classifier 设置

要使这个插件对Appium可用，只需转到主Appium repo，并运行npm install test-ai-classifier将这个插件安装到Appium的依赖树中，并使其可用。

否则，将它安装在文件系统的某个位置，并使用绝对路径作为模块名(参见下面)。

```shell
sudo npm --registry http://registry.npm.taobao.org install test-ai-classifier  --unsafe-perm
```

### 使用

1、启动appium

```
> appium
[Appium] Welcome to Appium v1.14.0
[Appium] Appium REST http interface listener started on 0.0.0.0:4723
...
```

2、编写自动化测试脚本：

```python
from appium import webdriver
from time import sleep


CAPS = {
    "deviceName": " MEIZU_E3",
    "automationName": "UiAutomator2",
    "platformName": "Android",
    "platformVersion": "7.1.1",
    "appPackage": " com.meizu.flyme.flymebbs",
    "appActivity": ".ui.LoadingActivity",
    "noReset": True,
    "unicodeKeyboard": True,
    "resetKeyboard": True,
    "customFindModules": {"ai": "test-ai-classifier"},
    "testaiConfidenceThreshold": 0.1,
    "shouldUseCompactResponses": False,
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', CAPS)
sleep(3)

# 用 AI 定位到搜索框
driver.find_element_by_custom("ai:search").click()
sleep(5)
driver.find_element_by_id("com.meizu.flyme.flymebbs:id/kf").send_keys("flyme")

driver.find_element_by_id("com.meizu.flyme.flymebbs:id/o7").click()
result = driver.find_elements_by_id("com.meizu.flyme.flymebbs:id/a2a")[0].text
print(result)

driver.quit()
```
