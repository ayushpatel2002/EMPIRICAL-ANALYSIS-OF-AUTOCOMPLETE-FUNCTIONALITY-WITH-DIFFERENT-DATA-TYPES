def sample25K():
    main_datafile = open("sampleData200k.txt", "r")
    smallSample = []
    sampleFile25k = open("Data25k.txt", "w")
    for line in main_datafile:
        smallSample.append(line)
        sampleFile25k.write(line)
        if len(smallSample) >= 25000:
            break


def sample50K():
    main_datafile = open("sampleData200k.txt", "r")
    mediumOneSample = []
    sampleFile50K = open("Data50k.txt", "w")
    for line in main_datafile:
        mediumOneSample.append(line)
        sampleFile50K.write(line)
        if len(mediumOneSample) >= 50000:
            break


# def sample75K():
#     main_datafile = open("sampleData200k.txt", "r")
#     mediumTwoSample = []
#     sampleFile75K = open("Data75K.txt", "w")
#     for line in main_datafile:
#         mediumTwoSample.append(line)
#         sampleFile75K.write(line)
#         if len(mediumTwoSample) >= 75000:
#             break


def sample100K():
    main_datafile = open("sampleData200k.txt", "r")
    mediumThreeSample = []
    sampleFile100K = open("Data100K.txt", "w")
    for line in main_datafile:
        mediumThreeSample.append(line)
        sampleFile100K.write(line)
        if len(mediumThreeSample) >= 100000:
            break


def sample125K():
    main_datafile = open("sampleData200k.txt", "r")
    largeSample = []
    sampleFile125K = open("Data125K.txt", "w")
    for line in main_datafile:
        largeSample.append(line)
        sampleFile125K.write(line)
        if len(largeSample) >= 125000:
            break


def sample150K():
    main_datafile = open("sampleData200k.txt", "r")
    largeOneSample = []
    sampleFile150K = open("Data150K.txt", "w")
    for line in main_datafile:
        largeOneSample.append(line)
        sampleFile150K.write(line)
        if len(largeOneSample) >= 150000:
            break


def sample175K():
    main_datafile = open("sampleData200k.txt", "r")
    largeTwoSample = []
    sampleFile175K = open("Data175K.txt", "w")
    for line in main_datafile:
        largeTwoSample.append(line)
        sampleFile175K.write(line)
        if len(largeTwoSample) >= 75000:
            if len(largeTwoSample) >= 175000:
                break


def main():
    sample25K()
    sample50K()
    sample100K()
    sample150K()
    sample175K()


if __name__ == "__main__":
    main()
