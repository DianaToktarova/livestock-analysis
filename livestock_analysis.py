import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_livestock_sheet(file_path, sheet_name):
    print(f"\n🔍 Анализ листа: '{sheet_name}'\n")
    
    # Загружаем данные (пропускаем первые 4 строки, как в оригинале)
    df = pd.read_excel(file_path, sheet_name=sheet_name, skiprows=4)

    # Очистка: переименование первого столбца
    df.rename(columns={df.columns[0]: "Показатель"}, inplace=True)
    df = df[df["Показатель"].notna()]  # убираем пустые строки

    # Преобразуем числовые столбцы
    for col in df.columns[1:]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    
    # Первичный анализ
    print("📌 head():")
    print(df.head())
    print("\n📌 info():")
    print(df.info())
    print("\n📌 describe():")
    print(df.describe())

    # Проверка пропущенных значений
    missing = df.isnull().sum()
    print("\n📌 Пропущенные значения по столбцам:")
    print(missing[missing > 0])

    # Визуализация: гистограмма по последнему году (если есть)
    numeric_cols = [col for col in df.columns if df[col].dtype in ['float64', 'int64']]
    if numeric_cols:
        last_col = numeric_cols[0]
        plt.figure(figsize=(12, 5))

        # Гистограмма
        plt.subplot(1, 2, 1)
        sns.histplot(df[last_col].dropna(), bins=10, kde=True, color='skyblue')
        plt.title(f"Гистограмма: {last_col}")
        plt.xlabel("Значение")
        plt.ylabel("Количество")

        # Bar chart — топ 10 значений
        plt.subplot(1, 2, 2)
        top_df = df.sort_values(by=last_col, ascending=False).head(10)
        plt.barh(top_df["Показатель"], top_df[last_col], color='royalblue')
        plt.title(f"Топ-10 показателей ({last_col})")
        plt.xlabel("Значение")
        plt.gca().invert_yaxis()

        plt.tight_layout()
        plt.show()
    else:
        print("❗Нет числовых столбцов для построения графиков.")

# 🔧 Пример вызова
file_path = r"C:\Users\tokta\proj1\proj1\livestock_kazakhstan_2024.xlsx"
analyze_livestock_sheet(file_path, "14.1")
