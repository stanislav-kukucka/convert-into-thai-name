### Defined thai letters and numbers
thaiAlpha = [' ', 'า', 'บ', 'ซ', 'ด', 'แ', 'ฟ', 'ก', 'ห', 'ิ', 'จ', 'ฅ', 'ล', 'ม',
 'น', 'อ', 'ภ', 'ข', 'ร', 'ส', 'ต', 'ึ', 'ฟ', 'ว', 'x', 'ย', 'ฉ'] # th
thaiNumber = ['๑', '๒', '๓', '๔', '๕', '๖', '๗', '๘', '๙', '๐'] # th
### Defined lating letters and numbers
latinAlpha = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
### Query your input
translateItToThai = input("Write your name in English: ")
def main():
    translationProcess = '---------- '
    if len(translateItToThai) > 0 :
        for n in translateItToThai.lower():
            if n in latinAlpha:
                translationProcess += thaiAlpha[latinAlpha.index(n)]
            elif n in numbers:
                translationProcess += thaiNumber[numbers.index(n)]
### Output of your input, translation
        print("---------- Your name in Thai is:");
        print(translationProcess)
        return
main()
