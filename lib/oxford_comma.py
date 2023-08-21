def oxford_comma(lst):
    if len(lst) == 1:
        return lst[0]

    elif len(lst) == 2:
        return f"{lst[0]} and {lst[1]}"

    else:
        formatted_list = ', '.join(lst[:-1])  # Join all elements except the last one with commas
        return f"{formatted_list}, and {lst[-1]}"  # Add the last element with "and"
