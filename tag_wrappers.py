def raw_text(string):
  return string

def p_wrapper(func):
  # func_wrapper_has access to func
  def func_wrapper(name):
    return '<p>{text}</p>'.format(text=func(name))
                                
  return func_wrapper

non_dec_p_wrapper = p_wrapper(raw_text)

@p_wrapper
def dec_p_wrapper(string):
  return string

def tag_wrapper(tag_name):
  # wrap_in_tags has access to tag_name
  def wrap_in_tags(func):
    # func_wrapper has access to func
    def func_wrapper(name):
      return '<{tag_name}>{text}</{tag_name}>'.format(text=func(name), 
                                                      tag_name=tag_name)
    return func_wrapper
  return wrap_in_tags

div_wrapper = tag_wrapper('div')
non_dec_div_wrapper = div_wrapper(raw_text)

@tag_wrapper('div')
def dec_div_wrapper(string):
  return string

def dynamic_wrapper(tag, string):
  @tag_wrapper(tag)
  def raw_text(string):
    return string

  return raw_text(string)

print dynamic_wrapper('strong', 'Example')

