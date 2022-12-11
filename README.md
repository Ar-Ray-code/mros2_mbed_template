# mros2_template

Template for mros2 (STM32, Mbed)

## Dockerでのビルド

注意！事前にDockerがインストールされているのを確認してください。

```bash
./build.py --target DISCO_F746NG
```

## 消去方法

.ccacheとcmake_buildディレクトリを消去します。

```bash
./build.py --clean
```