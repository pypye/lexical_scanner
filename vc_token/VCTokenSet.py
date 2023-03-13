IDENTIFIER="character(character|digit)*"
KEYWORD="boolean|break|continue|else|for|float|if|int|return|void|while"
ARITHMETIC="plus|minus|multiply|divide"
RELATIONAL="less|less_equal|greater|greater_equal"
LOGICAL="and|or|not"
EQUALITY="equal|not_equal"
ASSIGNMENT="assignment"
SEPARATOR="semicolon|comma|left_parenthesis|right_parenthesis|left_bracket|right_bracket|left_brace|right_brace"

INTLITERAL="digit(digit)*"

FRACTION = "(dot)(digit)+"
EXPONENT = "(E|e)(plus|minus)?(digit)+"
FLOATLITERAL=f"((digit)*({FRACTION})({EXPONENT}))" \
             f"|((digit)+(dot))"\
             f"|((digit)+(dot)?({EXPONENT}))"

BOOLEANLITERAL="true|false"
STRINGLITERAL="(double_quote)(character|digit|space)*(double_quote)"

