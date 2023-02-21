from imageCoordScanner import ImageCoordScanner
import inputs
from printer import Printer


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file = inputs.get_file()
    printer = Printer(inputs)
    ImageCoordScanner(file, printer)

