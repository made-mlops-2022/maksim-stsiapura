# Production ready project

## Установка виртуального окружения и необходимых библиотек для python3:
<code>
    ./scripts/create_python3_venv.sh
</code>

## Датасет:
<ol>
    <li>
        В папку ml_project/credentials нужно положить файлик kaggle.json c username и key для своего пользователя.
    </li>
    <li>
        Для скачивания данных нужно запустить скрипт:
        </br>
        <code>
            python scripts/download_dataset.py
        </code>
    </li>
</ol>

## EDA
Ноутбук по EDA: notebooks/heart-disease-dataset-cleveland-eda.ipynb. Чтобы сформировать отчет запустите скрипт:
</br>
<code>
    ./scripts/generate_eda_report.sh
</code>

## Модели:
Для прототипирования использовался ноутбук notebooks/heart-disease-logistic-regression-easy.ipynb. Алгоритмы для классификации: логистическая регрессия LogisticRegression и решающие деревья DecisionTreeClassifier из sklearn.