from spline import Spline


def main():
    spline = Spline('Points.txt')
    print(spline.dots, spline.dots_count)
    spline.get_polynomials()

    try:
        file = open('Result.txt', 'w', encoding='utf-8')
    except FileNotFoundError:
        print('Result file is nor founded')
        exit(2)

    for i in range(len(spline.polynomials)):
        print('F' + str(i+1) + '(x) = ' + str(spline.polynomials[i]))
        file.write('F' + str(i+1) + '(x) = ' + str(spline.polynomials[i]) + '\n')
    file.close()

    spline.get_plot()


main()