import pytest
from all_questions import *
import pickle



#-----------------------------------------------------------
def question1():
    answers = {}

    # type: float
    # Calculate the probability.
    answers['(a)'] = 0.0288

    # type: float
    # Calculate the probability.
    answers['(b)'] = 0.002

    # type: float
    # Calculate the probability.
    answers['(c)'] = 0.08
    return answers


#-----------------------------------------------------------
def question2():
    answers = {}

    # type: bool
    answers['(a) A'] = True

    # type: bool
    answers['(a) B'] = False

    # type: bool
    answers['(a) C'] = False

    # type: bool
    answers['(a) D'] = True

    # type: bool
    answers['(b) A'] = True

    # type: False
    answers['(b) B'] = False

    # type: bool
    answers['(b) C'] = True

    # type: bool
    answers['(b) D'] =  False
    # type: eval_float
    # The formulas should only use the variable 'p'. The formulas should be
    # a valid Python expression. Use the functions in the math module as
    # required.
    answers['(c) Weight update'] = "0.5*math.log((1-p)/p)"#0.4236

    # type: float
    # the answer should be correct to 3 significant digits
    answers['(d) Weight influence'] = 1.527
    return answers


#-----------------------------------------------------------
def question3():
    answers = {}

    # type: string
    answers['Agree?'] = "No"

    # type: explain_string
    answers['Explain'] = "Alan's strategy is ineffective because flipping a coin to make decisions is entirely based on chance and ignores pertinent stock market data. Ensemble methods, in contrast, enhance accuracy by integrating forecasts from multiple models, each of which performs better than mere randomness, unlike coin flipping."
    return answers


#-----------------------------------------------------------
def question4():
    answers = {}

    # type: bool
    answers['(a) e=0.5, independent'] = False

    # type: bool
    answers['(b), independent'] = True

    # type: bool
    answers['(c) identical'] = False
    return answers


#-----------------------------------------------------------
def question5():
    answers = {}

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(a)'] = "iii"

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(b)'] = "i"

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(c)'] = "ii"

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(d)'] = "iv"
    return answers


#-----------------------------------------------------------
def question6():
    answers = {}

    # type: eval_float
    answers['(a) C1-TPR'] = "p"

    # type: eval_float
    answers['(a) C2-TPR'] = "2*p"

    # type: eval_float
    answers['(a) C1-FPR'] = "p"

    # type: eval_float
    answers['(a) C2-FPR'] = "2*p"

    # type: string
    # choices: ['yes', 'no']
    answers['(b) C2 better classifier than C1?'] = 'no'

    # type: explain_string
    answers['(b) C2 better classifier than C1? Explain'] = (
           "C2 does not outperform C1 as a classifier since they both exhibit identical expected true positive rates (TPR) and false positive rates (FPR). This alignment places them on the random guess line of the ROC curve, indicating that their predictive ability does not exceed that of random chance."
           )

    # type: string
    # choices: ['TPR/FPR', 'precision/recall']
    answers['(c) Which metric?'] = 'precision/recall'

    # type: explain_string
    answers['(c) explain'] = (
        "In this case, precision and recall provide greater insight because they assess the proportion of accurate positive predictions (precision) and the model's capability to identify all positive instances (recall). Given that C2 has a superior recall compared to C1, it might be deemed a more effective classifier based on these measures."
    )

    return answers


#-----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    # choices: ['C1', 'C2', 'None']
    answers['(i) Best classifier?'] = 'C2'

    # type: explain_string
    answers['(i) Best classifier, explain'] = (
       "C2 is a superior classifier as it exhibits a significantly higher recall/TPR and F1-measure compared to C1, which shows it accurately identifies more positive cases and achieves a more effective balance between precision and recall."
    )

    # type: string
    # choices: ['TPR-FPR', 'precision-recall-F1-Measure']
    answers['(ii) appropriate metric pair'] = 'precision-recall-F1-Measure'

    # type: explain_string
    answers['(ii) appropriate metric pair, explain'] = (
        "Precision, recall, and F1-measure are suitable metrics for evaluating a classifier's performance as they offer a comprehensive view, particularly important in scenarios with imbalanced datasets where positive cases are significantly rarer than negative ones."
    )

    # type: string
    # choices: ['C1', 'C2', 'C3']
    answers['(iii) preferred classifier?'] = 'C2'

    # type: explain_string
    answers['(iii) best classifier, explain'] = (
       "C2 is favored because it achieves an optimal balance between precision and recall, as reflected by its superior F1-measure compared to other classifiers. Although C3 attains the highest precision, this comes at the cost of lower recall, making it less suitable in situations where detecting all positive cases is crucial."
    )

    return answers



#-----------------------------------------------------------
def question8():
    answers = {}

    # type: eval_float
    answers['(a) precision for C0'] = "p"

    # type: eval_float
    answers['(a) recall for C0'] = "p"

    # type: eval_float
    answers['(b) F-measure of C0'] = "2 * (0.1 * p) / (0.1 + p)"

    # type: string
    # choices: ['yes', 'no', 'unknown']
    answers['C1 better than random?'] = "yes"

    # type: float
    # What is the range of p for which C1 is better than random?  What is
    # "?" in the expression "p > ?"

    answers['p-range'] = 0.3
    return answers


#-----------------------------------------------------------
def question9():
    answers = {}

    # type: dict[string,float]
    # keys: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) metrics'] =  {
    'recall': 0.5333,
    'precision': 0.6154,
    'F-measure': 0.5714,
    'accuracy': 0.88
}

    # type: string
    # choices: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) best metric?'] = 'F-measure'

    # type: string
    # choices: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) worst metric?'] = 'accuracy'

    # type: explain_string
    answers['(ii) Explain your choices of best and worst metrics'] = (
       "In this situation, the F-measure is the most suitable metric because it balances precision and recall, essential in cases with imbalanced classes, like weather prediction where one outcome may predominate. Accuracy is the least effective metric, as it can be misleadingly high because of numerous true negatives, which does not truly reflect strong predictive ability for the less common class."
    )
    return answers


#-----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    # choices: ['T1', 'T2']
    answers['(a) better test based on F-measure?'] = "T1"

    # type: string
    # choices: ['T1', 'T2']
    answers['(b) better test based on TPR/FPR?'] = "T2"

    # type: string
    # choices: ['F1', 'TPR/FPR']
    answers['(c) Which evaluation measure to use between the two tests?'] = "TPR/FPR"

    # type: explain_string
    answers['(c) Which evaluation measure? Explain'] = (
        "In medical settings where the substantial consequences of missing a diagnosis (false negatives) surpass the implications of false positives, TPR/FPR becomes the optimal metric for assessing cancer detection tests T1 and T2. This emphasizes the critical need for the test to accurately identify true positive cases."
    )

    # type: explain_string
    answers['(d) Example scenario where you would reverse choise in (c)'] = (
        "When screening a population with a very low likelihood of having cancer (low prevalence), the F-measure might be preferable to TPR/FPR due to the significant impact of false positives. These can cause psychological distress, expose individuals to risky procedures, or lead to high costs from unnecessary diagnostic treatments. The F-measure, which considers both true positives and false positives, is advisable in this context. Prioritizing the F-measure is particularly important when follow-up procedures after a positive test are costly, invasive, or risky, to ensure the test’s precision minimizes the occurrence of false positives."
    )

    return answers
#-----------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
