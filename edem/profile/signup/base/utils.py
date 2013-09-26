# coding=utf-8
#from Products.GSProfile.utils import escape_c
import string

def fn_to_nickname(context, fn):
    """Display Name to Nickname
    
    DESCRIPTION
        Convert a display name into a nickname. 
    ARGUMENTS
        "context":  The current context; used to get the user-folder.
        "fn":       The name to convert.
    
    RETURNS
        A string, which is not used as either the user-name or user-ID
        name of an existing user of the system. White-space is removed,
        illegal characters are escaped, and a number is added to the end
        to ensure uniqueness.
    
    SIDE EFFECTS
        None.
    
    """
    unstrippednick = ''.join([c for c in unicode(''.join(fn.split()).lower())])
    nickname = ''
    for char in unstrippednick:
        if char in string.printable:
            nickname += char
    origNickname = nickname
    acl_users = context.acl_users
    i = 1
    while (acl_users.getUser(nickname) 
           or acl_users.get_userByNickname(nickname)):
        nickname = origNickname + unicode(i)
        i = i + 1

    assert type(nickname) == unicode
    assert not(acl_users.getUser(nickname))
    assert not(acl_users.get_userByNickname(nickname))

    return nickname

