IDENTIFIER="character(character|digit)*"
KEYWORD="boolean|break|continue|else|for|float|if|int|return|void|while"
ARITHMETIC="plus|minus|multiply|divide"
RELATIONAL="less|less_equal|greater|greater_equal"
LOGICAL="and|or|not"
EQUALITY="equal|not_equal"
ASSIGNMENT="assignment"
SEPARATOR="semicolon|comma|left_parenthesis|right_parenthesis|left_bracket|right_bracket|left_brace|right_brace"

INTLITERAL="digit(digit)*"

__FRACTION__ = "(dot)(digit)+"
__EXPONENT__ = "(E|e)(plus|minus)?(digit)+"
FLOATLITERAL=f"((digit)*({__FRACTION__})({__EXPONENT__}))" \
             f"|((digit)+(dot))"\
             f"|((digit)+(dot)?({__EXPONENT__}))"

BOOLEANLITERAL="true|false"
STRINGLITERAL="(double_quote)(character|digit|space)*(double_quote)"

