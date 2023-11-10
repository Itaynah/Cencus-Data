import csv
import json
age = []
sex = []
bmi = []
children = []
smoker = []
region = []
charges = []


def csv_to_list(lst, file, column_name):
    with open(file) as ins:
        dict_reader = csv.DictReader(ins)
        for row in dict_reader:
            lst.append(row[column_name])
    return lst


csv_to_list(age, "insurance.csv", 'age')
csv_to_list(sex, "insurance.csv", 'sex')
csv_to_list(bmi, "insurance.csv", 'bmi')
csv_to_list(children, "insurance.csv", 'children')
csv_to_list(smoker, "insurance.csv", 'smoker')
csv_to_list(region, "insurance.csv", 'region')
csv_to_list(charges, "insurance.csv", 'charges')


# average age of clients by their number of children,
# inserting -1 in "child" parameter will calculate the average age regardless to number of children
def avg_age_by_child(age, children, child=-1):
    sum_age = 0
    count = 0
    zipped = zip(age, children)
    for item in zipped:
        if child < 0:
            sum_age += int(item[0])
            count += 1
        elif child == int(item[1]):
            sum_age += int(item[0])
            count += 1
    if child == -1:
        child = "any and/or no"
    if sum_age == 0:
        return "There's no such a record for the given number of children"
    return "The Average age of clients who has " + str(child) + " children is: " + str(round(sum_age / count, 2))


def average_cost_if_smoke(charges, smoker):
    zipped = zip(charges, smoker)
    total, smoker, non_smk, count, non_count = 0, 0, 0, 0, 0
    for item in zipped:
        total += float(item[0])
        if item[1] == "yes":
            smoker += float(item[0])
            count += 1
        else:
            non_smk += float(item[0])
            non_count += 1
    total /= len(charges)
    smoker /= count
    non_smk /= non_count
    percentage_increase = ((smoker - non_smk) / non_smk) * 100
    return ("The average yearly insurance charges is: " + str(
        round(total,2)) + "$.\nThe average yearly insurance charges for smoker is: " + str(round(smoker,2)) +
            "$.\nThe average yearly insurance charges for non-smoker is: " + str(round(non_smk,2)) + "$." +
            "\nOn average, the charges for smokers are " + str(round(percentage_increase,2)) + "% more expensive.")

def sex_balance(sex):
    f_count, m_count = 0,0
    for item in sex:
        if item == "female":
            f_count += 1
        else:
            m_count += 1
    return ("There are "+ str(f_count)+" females and "+str(m_count)+" males\nfamales make "+
            str(round(f_count/len(sex), 2))+"% of the clients.")


def highest_children_rate(children, region):
    region_uniq = set(region)
    region_dict = {key: 0 for key in region_uniq}
    zipped = zip(children, region)
    for item in zipped:
        region_dict[item[1]] = region_dict.get(item[1]) + int(item[0])
    max_value = max(region_dict.values())
    for key in region_dict.keys():
        if region_dict[key] == max_value:
            region_max = key
    return ("The max children rate is "+str(max_value) + " coming from the "+ region_max +".\n"
            "Here's the deviation of children among the regions:\n" + str(region_dict) )


