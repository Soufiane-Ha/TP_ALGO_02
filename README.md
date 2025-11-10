# TP_ALGO_02
-------------------------------------------------
>  Required Algorithmes :

1- tri par Sélection

2- tri a bulles.

3- tri par insertion (échanger).

4- tri par insertion (déplacement).

> Critères:

1- Nombre de comparaisons.

2- Nombre de déplacement.

3- temps d'execution.

Objectives:

1- Implementer les algorithmes.

2- Comparer les algoritmes Par les critéres.

3- Analyse l'impact de la disposition initial de données (trié croissant, trié décroissant, aléatoire)

4- Analyse des résultats :

- Comparer l’influence du classement initial des résultats sur le résultat final.

- Identifier l’algorithme le plus performant pour chaque type de configuration.

- Déterminer si les résultats expérimentaux confirment la complexité théorique des TD.

> Instruction.

#écrit me fonction qui permet de générer des tableaux de grandes tailles (10^5/10^6/10^7) et diffisent dispontion initiales:

```void generate Table (int * tab, int n ,cher dis) dis € {'A','C','D'}```

#excaster plus de 30 a tests de differents tailles aleatais pour chaque algorithms (collecter le moyen de critères)

#Organisées les roultet das un tableau comprentatif on dans un graphe.

> Fountion Time
```
time.Perf-counter-ns()
```

> Analyse de resultat
## Franch
Il s'agit d'une méthode de recherche (tri) efficace, et chacune présente ses propres avantages en termes de :

Temps d'exécution :

Chaque algorithme a un temps d'exécution spécifique, et celui qui s'exécute le plus rapidement est considéré comme le meilleur.

Nombre de comparaisons :

Le nombre d'opérations constitue le second facteur, car il influe considérablement sur la complexité de l'algorithme. Cette complexité, à son tour, influe sur le temps d'exécution.

Impact du tri initial sur le résultat final

Le tri initial des données influe directement sur les performances des quatre algorithmes de tri :

Tableau pré-trié (cas favorable) :

Le tri à bulles et le tri par insertion sont extrêmement rapides grâce au faible nombre de comparaisons et d’échanges effectués lors du tri.

Le tri par sélection reste pratiquement inchangé en termes de comparaisons (leur nombre demeure identique), car il parcourt toujours l’intégralité du tableau, même s’il est déjà trié. Autrement dit, si le tableau est déjà trié, il effectue une nouvelle vérification sans modification.

Le tri par transfert bénéficie également du tri initial, mais son amélioration est modérée.

Tableau inversé (cas défavorable) :

Le tri à bulles devient le plus lent : il effectue le nombre maximal d’échanges à chaque passage sur l’ensemble du tableau.

Le tri par insertion effectue également un grand nombre de transferts sur l’ensemble du tableau.

Le tri par sélection reste stable grâce au nombre constant de comparaisons, mais il demeure lent en raison des multiples recherches de la valeur minimale.

Le tri par échange/déplacement présente un comportement intermédiaire, selon sa méthode d'implémentation.

Tableau aléatoire (cas intermédiaire) :

Les performances se situent entre les extrêmes.

Le tri par insertion est généralement plus performant sur les tableaux semi-ordonnés.

Le tri à bulles reste généralement le moins efficace.

2. Algorithmes les plus efficaces selon le type de configuration

| Type de tableau  | Algorithme le plus rapide | Remarques |
| ------------- | ------------- | ------------- |
| Tri par insertion  | pré-ordonné  | Très peu de déplacements requis |
| Tri par sélection  | inversé  | Comparaisons fixes, indépendantes de l'ordre initial |
| Tri par insertion ou par échange  | aléatoire  | Bon compromis entre comparaisons et déplacements |

## Arabic

هذه إحدى طرق البحث (الفرز) الفعّالة، ولكلٍّ منها مزاياها الخاصة من حيث :

زمن التنفيذ :

لكل خوارزمية زمن تنفيذ محدد، وما يميزها هو أقصر زمن تنفيذ التي تعتبر هي أفضل خوارزمية.

عدد المقارنات :

العامل الثاني و هو عدد العمليات الذي يؤثر بشكل كبير على مدى تعقيد الخوارزمية يؤثر ذلك على زمن التنفيذ أيضا

تأثير الفرز الأولي على النتيجة النهائية

يؤثر الترتيب بشكل الأولي للبيانات بشكل مباشر على أداء خوارزميات الفرز الأربعة :

المصفوفة المُفرزة مسبقًا (حالة مواتية):

يتميز فرز الفقاعات وفرز الإدراج بسرعة فائقة في الميكانيزم العمل نظرًا لقلة عدد المقارنات والتبادلات خلال الفرز.

يبقى فرز التحديد دون تغيير تقريبًا من حيث المقارنات (تبقى نفسها)، إذ لا يزال يجتاز المصفوفة بأكملها حتى لو كانت مُفرزة بالفعل أي إذا كانت أصلا المصفوفة مرتبة سيعيد التحقق دون إطراء اي تغير.

يستفيد فرز التبديل/النقل أيضًا من الترتيب الأولي، ولكن تحسنه متوسط.

المصفوفة المقلوبة (حالة غير مواتية):

يصبح فرز الفقاعات الأبطأ: إذ يُجري أقصى عدد من التبادلات في كل تمريرة على جميع السلسلة.

يُجري فرز الإدراج أيضًا عددًا كبيرًا من عمليات النقل على طول السلسلة بأكملها.

يبقى فرز التحديد مستقرًا لثبات عدد المقارنات، ولكنه يظل بطيئًا بسبب عمليات البحث المتعددة عن الحد الأدنى للقيمة.

يُظهر فرز التبديل/النقل سلوكًا متوسطًا، حسب طريقة التنفيذ.

مصفوفة عشوائية (حالة متوسطة):

يقع الأداء بين النقيضين.

يميل فرز الإدراج إلى أن يكون أفضل في المصفوفات شبه المرتبة.

يظل فرز الفقاعات الأقل كفاءةً بشكل عام.

2. أكثر الخوارزميات كفاءةً وفقًا لنوع التكوين

| نوع المصفوفة  | أسرع خوارزمية | ملاحظات |
|-------- | -------- |--------|
| مرتبة مسبقًا  | فرز الإدراج  | عدد الحركات المطلوبة قليل جدًا |
| مقلوب  | فرز التحديد  | مقارنات ثابتة، لا تعتمد على الترتيب الابتدائي |
| عشوائي  | فرز الإدراج أو التبديل  | حل وسط جيد بين المقارنات والحركات |
