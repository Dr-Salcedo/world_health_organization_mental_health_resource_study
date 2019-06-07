# World Health Organization Mental Health Resource Study
==============================

A Statistical Analysis of  Mental Health Resources and Global Suicide Rates
==============================


### Background

There is a lot of present day media coverage as well as general discussion surrounding mental health care and the allocation of resources for treatment. It is estimated, as of 2017, that about 13% (11-18%) of the global population has a mental health or substance abuse disorder, with the top two illnesses being depression and anixety. 

Whether people with mental health illnesses have access to adequate mental heatlh resources and whether these resources are effective is critical.  The effective treatment of mental health illness has wide-ranging implications on society as a whole to individual businesses.  The mental well-being and by extension, productivity, of a population should be of concern to everyone.  Those in the position to affect mental health policies and resource allocation may find this analysis useful.

### Design and Methods

We utilized the World Health Organization's "Global Health Observatory Data Repository" to study and analyze the availablity of mental health resources and the effectivness of these resources in treating and alleviating mental health illnesses.  Suicide rate was utilized as a proxy for resource effectiveness because it was the only easily quantifiable variable across all countries.  We should also note that mental health disorders are not only numerous and diverse, but in many instances overlapping. For the data utilized and our analysis, we refer to mental health disorders in accordance with WHO's International Classification of Diseases (ICD-10). Mental health disorders encompassed by the ICD-10 include, but are not limited to depression, generalized anxiety, bipolar d/o, sichzophrenia, and eating disorders.

Given that it is widely accepted that there are stark differences in available resources as well as reported rates of mental health illnesses among various countries, we chose to investigate specifically, if there is a relationship between the total number of available mental health providers in a given country and reported suicide rates.  For this analysis, mental health providers included psychiatrists, psychologists, social workers, and dedicated mental health nurses.  

Each provider type was given equal weight in the analysis and a tally count of total mental health provider obtained.  A mean threshold for provider count for all countries was calculated and used to divide all countries into 2 groups.  Group 1 being the high resource group and group 2 being the low resource group.  The age range utilized in this study included individuals ages 15-29.  All countries for which suicide rates and provider statistics were available for the year 2016 were included in the analysis.  In order to obtain a normal sampling distribution from which to conduct our analysis, the sample data was bootstrapped (ie repeated sampling of our data with replacement) 1000 times with a sample size of 500 (n=500).  Three hypotheses were tested via 2 sample independent T-Tests in our analysis.  In addition to computing p-values for alternative hypothesis testing, effect size and distribution visualizations were utilized.

Hypotheses:

1) There is a difference in suicide rates for countries below and above the mean threshold of mental health providers per 100,000 people.

Note: mental health providers include psychiatrists, psychologists, dedicated mental health nurses, social workers.

2) There is a difference in suicide rates for males in countries below and above the mean threshold of mental health professionals per 100,000 people.


3) There is a difference in suicide rates for females in countries below and above the mean threshold of mental health professionals per 100,000 people.


### Results

Hypothesis 1: There is a difference in suicide rates for countries below and above the mean threshold of mental health providers per 100,000 people.

    With p=0.00, we can reject the Null Hypothesis. These populations are different.
    Effect size (Cohen's D): 0.1593
    
    ![alt text](/images/raw_dist_btsx.png)            ![alt text](/images/bootstrap_dist_btsx.png)       
    

Hypothesis 2: There is a difference in suicide rates for males in countries below and above the mean threshold of mental health professionals per 100,000 people.

    With p=0.00, we can reject the Null Hypothesis. These populations are different.
    Effect size (Cohen's D): 0.284

     ![alt text](/images/raw_dist_males.png)            ![alt text](/images/bootstrap_dist_males.png)  
     
     
     
Hypothesis 3:There is a difference in suicide rates for females in countries below and above the mean threshold of mental health professionals per 100,000 people.

    With p=0.00, we can reject the Null Hypothesis. These populations are different.
    Effect size (Cohen's D): 0.266

     ![alt text](/images/raw_dist_females.png)            ![alt text](/images/bootstrap_dist_females.png)  
     
     

### Interpretation

For our first hypothesis, we calculated a Cohen's D of 0.1593, demonstrating a signficant (p=0.00), albeit small, relationship beteewn a country's suicide rate and available mental healthcare providers.

Upon graphing the low resource and high resource groups, we observed a higher mean distribution of suicide rates in high resource countries and a lower mean distribution of suicide rates in low resource country.

This result is counterintuitive and may be reflective of several factors.  Firstly, suicide rates may not be the best proxy for mental health resource effectiveness.  It fails to take into account the great deal of variety in mental health classification.  Mental health illnesses such as generalized anxiety and eating disorders can expectedly have far less correlation to suicide rates.  Furthermore, available resources may be very effective in treating mental health illnesses and alleviating patient symptoms, however this would not be reflected in our model.

It is also important to note that suicide reporting is not standardized across all countries.  It is true that the WHO recognizes a greater occcurrence of under-reporting and misclassificaiton of suicides in low and middle income countries, which undoubtedly skews data for the low resource sample group.

The acceptance of suicide in various cultures and religions, and by extenstion countries, also differs significantly throughout the world.  For instance, in several countries, suicide is illegal and failed suicide attempts can even result in prison time and successfull suicides can result in fines and ostracization of surviving relatives.  These factors lead some countries, such as North Korea, to have some of the lowest suicide rates in the world.



For our second hypothesis, we calculated a Cohen's D of 0.284, demonstrating a signficant (p=0.00), albeit small, relationship beteewn a country's male suicide rate and available mental healthcare providers.

Upon graphing the low resource and high resource groups, we observed a higher mean distribution of male suicide rates in high resource countries and a lower mean distribution of male suicide rates in low resource country.


For our third hypothesis, we calculated a Cohen's D of 0.266, demonstrating a signficant (p=0.00), albeit small, relationship beteewn a country's female suicide rate and available mental healthcare providers.

Upon graphing the low resource and high resource groups, we observed a lower mean distribution of female suicide rates in high resource countries and a higher mean distribution of female suicide rates in low resource countries.


This seemingly paradoxical result may have been obtained for several reasons.  In addition to aforementioned country specific differences in the population samples, differences between female and male suicide methods and resulting intervention times could have skewed the data.  It is widely known that the methods of which men and female commit suicides differ greatly.  While the top methods of suicide for males, according to WHO, inlcude firearm use and hanging, for females the most prevalent method of sucicide involves some form of poisoning (medications, pesticides, etc).  This factor alone is very important to consider.  In abrupt suicide methods where no time is provided for possible medical intervetion, it is resonable to expect higher suicide rates.  In suicide attempts that allow time for intervention and treatment, there is a greater opportunity for the preservation of life and thus a lower suicide rate.  Based on the results obtained for the female population comparison, one could conclude that available resources, when given appropriate time to be utilized, are effective in reducing suicide rates.




### Recommendations and Potential Further Study

The value of addressing and treating mental health illness in society cannot be overstated. 

From a research perspective, futher comparative research analyses on the predictive factors influencing mental health in low and middle income countries are needed.  It is with this research that we will be in a better position to effectively treat and alleviate mental health illnesses.

A more standardized and uniform data collection and classification system for mental health illness, although difficult, would allow for the elimination or at least minimization of various variables such as differences in country specific laws and societal norms.  This would allow for more direct and reliable statistical studies.

From a business perspective, the effectiveness of mental health intervention in improving workers' quality of life and preventing suicides is well documented.  How to most effectivley allocate resources toward mental health illness still requires further study.  An example being finding more effective suicide prevention methods for males, who compose a population more likely compared to females to engage in abrupt suicide methods.


*****************************************
### Sources

World Health Organization's "Global Health Observatory Data Repository"

Hannah Ritchie and Max Roser (2019) - "Mental Health". Published online at OurWorldInData.org. Retrieved from: 'https://ourworldindata.org/mental-health' [Online Resource]
