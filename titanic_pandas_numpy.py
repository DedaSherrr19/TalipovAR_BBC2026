import pandas as pd
import numpy as np

df=pd.read_csv("tested.csv")#6

n=int(input('сколько первых строк вывести: '))
print('первые строки\n',df.head(n))#7
print('последние 5 строк\n',df.tail(5))#8
print('строк',df.shape[0],'столбцов',df.shape[1])#9
print('названия столбцов',df.columns.tolist())#10
print('типы данных\n',df.dtypes)#11

numbers=['Age','SibSp','Parch','Fare']
category=['Survived','Pclass','Sex','Embarked']

print('числовые признаки',numbers)#12
print('категориальные признаки',category)
print('идентификатор: PassengerId')
print('имя и обозначения: Name, Ticket, Cabin')

print('статистика\n',
      df[numbers].agg(['mean','median','min','max','std']))#13

print('пассажиры по классам\n',
      df['Pclass'].value_counts().sort_index())#14

print('уникальных портов',df['Embarked'].nunique())#15

print('класс — категория с порядком, а не количественная величина')


# пропуски

size_before=df.shape

missing=df.isna().sum()
print('пропуски\n',missing)#16

print('процент пропусков\n',missing/len(df)*100)#17
print('больше всего пропусков',missing.idxmax())#18

age_before=df['Age'].agg(
    ['mean','median','min','max','std','count']
)
print('возраст до заполнения\n',age_before)#19

df['Age']=df['Age'].fillna(df['Age'].median())#20

age_after=df['Age'].agg(
    ['mean','median','min','max','std','count']
)
print('возраст после заполнения\n',age_after)#21

age_comparison=pd.DataFrame({
    'до':age_before,
    'после':age_after
})
age_comparison.index=[
    'среднее','медиана','минимум',
    'максимум','стандартное отклонение','известных значений'
]
print('сравнение возраста\n',age_comparison)#22

df=df.dropna(subset=['Embarked'])#23

cabin_percent=df['Cabin'].isna().mean()*100
print('пропусков в Cabin, %',cabin_percent)

if cabin_percent>50:
    df=df.drop(columns=['Cabin'])
    print('столбец Cabin удалён')#24

print('оставшиеся пропуски\n',df.isna().sum())#25
print('размер до',size_before,'размер после',df.shape)#26

print('27. медиана менее чувствительна к выбросам')

print('28. изменения:')
for name in age_before.index:
    if np.isclose(age_before[name],age_after[name]):
        print(name,'не изменилось')
    else:
        print(name,'изменилось')

print('29. заполнение медианой меняет разброс значений')

print('30. распределение меняется: значений у медианы становится больше')


# numpy

survived=df['Survived'].to_numpy()
sex=df['Sex'].to_numpy()
age=df['Age'].to_numpy()
fare=df['Fare'].to_numpy()

print('выживших, %',np.mean(survived)*100)#31

male=sex=='male'
female=sex=='female'

male_survival=np.mean(survived[male])*100
female_survival=np.mean(survived[female])*100

print('выживших мужчин, %',male_survival)#32
print('выживших женщин, %',female_survival)

male_age=np.mean(age[male])
female_age=np.mean(age[female])

print('средний возраст мужчин',male_age)#33
print('средний возраст женщин',female_age)

rows=[]

for gender in ['male','female']:
    for status in [0,1]:
        mask=(sex==gender)&(survived==status)

        if np.any(mask):
            mean_age=np.mean(age[mask])
        else:
            mean_age=np.nan

        rows.append({
            'пол':gender,
            'выжил':status,
            'количество':np.sum(mask),
            'средний возраст':mean_age
        })

print('возраст по группам\n',pd.DataFrame(rows))#34

print('минимальная цена',np.nanmin(fare))#35
print('максимальная цена',np.nanmax(fare))
print('средняя цена',np.nanmean(fare))

print('стандартное отклонение возраста',
      np.std(age,ddof=1))#36

comparison=pd.DataFrame({
    'пол':['мужчины','женщины'],
    'количество':[np.sum(male),np.sum(female)],
    'выживших, %':[male_survival,female_survival],
    'средний возраст':[male_age,female_age]
})
print('сравнение\n',comparison)

print('разница выживаемости, п. п.',
      female_survival-male_survival)
print('разница возраста мужчин и женщин',male_age-female_age)

if np.array_equal(survived,female.astype(int)):
    print('в этом файле Survived определяется полом; '
          'для реальных выводов нужны фактические исходы')


# фильтрация

result1=df[
    (df['Sex']=='male')&
    (df['Age']>30)&
    (df['Pclass']==1)
]
print('задание 1, количество',len(result1))
print(result1.head(10))

result2=df[
    ((df['Age']<18)|(df['Sex']=='female'))&
    (df['Survived']==1)
]
print('задание 2, количество',len(result2))

third_class_mean=df.loc[df['Pclass']==3,'Fare'].mean()

result3=df[
    (df['Pclass']==3)&
    (df['Fare']>third_class_mean)
]
print('задание 3, количество',len(result3))
print(result3)

result4=df[
    (df['Age']>=20)&
    (df['Age']<=40)&
    (df['Embarked']=='S')
]
print('задание 4, количество',len(result4))
print(result4)

print('и (&) — все условия, или (|) — хотя бы одно')


# группировка

statistics=df.groupby(['Pclass','Sex']).agg(
    количество=('PassengerId','size'),
    средний_возраст=('Age','mean'),
    выживших_процент=('Survived','mean'),
    средняя_цена=('Fare','mean')
)

statistics['выживших_процент']*=100
print('по классу и полу\n',statistics)#37

ports=df.groupby('Embarked').agg(
    количество=('PassengerId','size'),
    выживших_процент=('Survived','mean')
)

ports['выживших_процент']*=100
print('по портам\n',ports)#38

class_survival=df.groupby('Pclass')['Survived'].mean()*100

best_classes=class_survival[
    class_survival==class_survival.max()
].index.tolist()

print('выживаемость по классам\n',class_survival)#39
print('класс с наибольшей выживаемостью',best_classes)

print('фильтрация выбирает строки, группировка объединяет '
      'их для расчёта показателей')


# сохранение

df.to_csv('titanic_processed.csv',index=False)#40
print('обработанные данные сохранены')

statistics.to_csv('titanic_statistics.csv')#41
print('статистика сохранена')

df_check=pd.read_csv('titanic_processed.csv')

pd.testing.assert_frame_equal(
    df.reset_index(drop=True),
    df_check,
    check_exact=False,
    rtol=1e-9,
    atol=1e-9
)#42
print('данные сохранены корректно')


# выводы

print('43. больше всего пропусков',missing.idxmax())

print('44. размер до',size_before,'после',df.shape)
print(age_comparison)

print('45. выживших мужчин, %',male_survival)
print('выживших женщин, %',female_survival)
print('показатели относятся к значениям этого файла')

print('46. наибольшая выживаемость в классе',best_classes)

print('47. полезны фильтрация, обработка пропусков, '
      'группировка и расчёты numpy')