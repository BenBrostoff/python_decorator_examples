def raw_text(string):
  return string


##############################
# TIPS ON DECORATOR FNS#
# 1. Pass in the fn as a param
# 2. Pass in params in the inner fn
#    - remember you have access to the outer scope! (passed in fn)
# 2. Return the fn after modifying it
##############################

def p_wrapper(func):
    def fn_wrapper(name):
        return '<p>{text}</p>'.format(text=func(name))
    return fn_wrapper


non_dec_p_wrapper = p_wrapper(raw_text)

# TODO - add decorator here
@p_wrapper
def dec_p_wrapper(string):
    return string

def tag_wrapper(tag_name):
    def tag_selector(func):
        def fn_wrapper(name):
            return '<{tag_name}>{text}</{tag_name}>'.format(text=func(name),
                                                            tag_name=tag_name)
        return fn_wrapper
    return tag_selector


div_wrapper = tag_wrapper('div')
non_dec_div_wrapper = div_wrapper(raw_text)


@div_wrapper
def dec_div_wrapper(string):
    return string


def dynamic_wrapper(tag, string):
    """
    :param tag: desired HTML tag
    :param string: string to wrap in tag
    :return: string wrapped in tag
    """
    @tag_wrapper(tag)
    def wrap(string):
        return string

    return wrap(string)

