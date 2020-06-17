def main():
    print("Ten program liczy, ile będziesz musiał(a) odprowadzić podatku VAT od sprzedaży")
    przychod =input("Podaj swoje dochody (bez waluty): ")
    odprowadzone = przychod - 0.23%
    print()
if __name__ == '__main__':
    main()
