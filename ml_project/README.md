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
            python src/data/download_dataset.py
        </code>
    </li>
    <li>
        Давайте подготовим искусственные данные с помощью скрипта (разделим на test и train):
        </br>
        <code>
            python src/data/prepare_data.py
        </code>
        </br>
    </li>
</ol>

## EDA
Ноутбук по EDA: notebooks/heart-disease-dataset-cleveland-eda.ipynb. Чтобы сформировать отчет запустите скрипт:
</br>
<code>
    ./scripts/generate_eda_report.sh
</code>

## Модели:
Для прототипирования использовался ноутбук notebooks/heart-disease-logistic-regression-easy.ipynb. Алгоритмы для классификации: логистическая регрессия LogisticRegression и решающие деревья DecisionTreeClassifier из sklearn. Оценки моделей находятся в данном ноутбуке.
</br>

В коде программы реализована возможность сделать fit и predict, никакой оценки, так как в реальной жизни зачастую мы не имеет таргеты для тестовой выборки. Ну а если и имеем, то давайте оценивать их в соотвествующем ноутбуке :)
</br>

Можем обучить модельку и положить ее в отдельную папку models:
</br>
<code>
    python src/main.py --fit \\  
                       --X_train "data/X_train.csv" \\  
                       --y_train "data/y_train.csv" \\  
                       --model_path "models/model.sav"
</code>
</br>

Можем сделать fit с помощью конфига:
</br>
<code>
    python src/main.py --fit \\  
                       --config configs/log_reg_config.yaml
</code>
</br>

И сделать предсказание:
</br>
<code>
    python src/main.py --predict \\  
                       --model_path "models/model.sav" \\  
                       --X_test "data/X_test.csv" \\  
                       --y_test "data/y_test.csv"                
</code>

## Тесты:
Для запуска всех тестов нужно запустить скрипт:
</br>
<code>
    ./scripts/run_tests.sh
</code>