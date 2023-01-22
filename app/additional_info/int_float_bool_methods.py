int_bool_methods = {
    "as_integer_ratio": """
        Return integer ratio.
        
        Return a pair of integers, whose ratio is exactly equal to the original int
        and with a positive denominator.
        
        >>> (10).as_integer_ratio()
        (10, 1)
        >>> (-10).as_integer_ratio()
        (-10, 1)
        >>> (0).as_integer_ratio()
        (0, 1)
        """,
    "bit_count": """
        Number of ones in the binary representation of the absolute value of self.
        
        Also known as the population count.
        
        >>> bin(13)
        '0b1101'
        >>> (13).bit_count()
        3
        """,
    "bit_length": """
        Number of bits necessary to represent self in binary.
        
        >>> bin(37)
        '0b100101'
        >>> (37).bit_length()
        6
        """,
    "conjugate": """ Returns self, the complex conjugate of any int. """,
    "denominator": """the denominator of a rational number in lowest terms""",
    "from_bytes": """
        Return the integer represented by the given array of bytes.
        
          bytes
            Holds the array of bytes to convert.  The argument must either
            support the buffer protocol or be an iterable object producing bytes.
            Bytes and bytearray are examples of built-in objects that support the
            buffer protocol.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Indicates whether two's complement is used to represent the integer.
        """,
    "imag": """the imaginary part of a complex number""",
    "numerator": """the numerator of a rational number in lowest terms""",
    "real": """the real part of a complex number""",
    "to_bytes": """Return an array of bytes representing an integer.
        
          length
            Length of bytes object to use.  An OverflowError is raised if the
            integer is not representable with the given number of bytes.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Determines whether two's complement is used to represent the integer.
            If signed is False and a negative integer is given, an OverflowError
            is raised.
        """,
}

float_methods = {
    "as_integer_ratio": """
        Return integer ratio.
        
        Return a pair of integers, whose ratio is exactly equal to the original float
        and with a positive denominator.
        
        Raise OverflowError on infinities and a ValueError on NaNs.
        
        >>> (10.0).as_integer_ratio()
        (10, 1)
        >>> (0.0).as_integer_ratio()
        (0, 1)
        >>> (-.25).as_integer_ratio()
        (-1, 4)
        """,
    "conjugate": """ Return self, the complex conjugate of any float. """,
    "fromhex": """
        Create a floating-point number from a hexadecimal string.
        
        >>> float.fromhex('0x1.ffffp10')
        2047.984375
        >>> float.fromhex('-0x1p-1074')
        -5e-324
        """,
    "hex": """
        Return a hexadecimal representation of a floating-point number.
        
        >>> (-0.1).hex()
        '-0x1.999999999999ap-4'
        >>> 3.14159.hex()
        '0x1.921f9f01b866ep+1'
        """,
    "imag": """the imaginary part of a complex number""",
    "is_integer": """ Return True if the float is an integer. """,
    "real": """the real part of a complex number""",
}
