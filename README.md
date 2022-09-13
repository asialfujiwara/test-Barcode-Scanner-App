# Appiumを使ったモバイルアプリのUIテスト自動化

Monacaサンプルアプリのテスト自動化サンプル

## Overview

Monacaプラグイン `@monaca/monaca-plugin-barcode-scanner` のサンプルアプリの
UI自動のサンプルコードです。

## Structure

```
.- Monacaサンプルプロジェクト
|- README.md
|- LICENSE
|- test テストコード
    |- util.py  初期設定
    |- test_android.py  テストコード
    |- setup.cfg  deprecated warning対応
    |- screenshots  スクリーンショット保存ディレクトリ
```
## Requirement

- Monaca
- [appium](https://github.com/appium/appium-desktop)
- pytest + [appium client+α](https://github.com/appium/appium/blob/1.x/sample-code/python/requirements.txt)
- Android Studio + emulator

## Usage

1. このリポジトリをMonacaにインポート
2. デバッグビルド
3. 出力結果をダウンロード
4. test/app-debug.apk として配置
5. Appiumサーバ起動
6. testディレクトリで pytest test_android.py 実行

## LICENSE

see [LICENSE](./LICENSE)
