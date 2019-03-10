# C

```c
/*
 * Assertions
 */

#define ASSERT_GENERAL(exp, msg, exe) \
if (!(exp)) {                         \
    printf(msg);                      \
    exe;                              \
}

#define ASSERT_RETURN(exp, msg, status) ASSERT_GENERAL(exp, msg, return status)
#define ASSERT_EXIT(exp, msg, status)   ASSERT_GENERAL(exp, msg, exit(status))
#define ASSERT_BREAK(exp, msg)          ASSERT_GENERAL(exp, msg, break)
#define ASSERT_CONTINUE(exp, msg)       ASSERT_GENERAL(exp, msg, continue)

/*
 * Bit Manipulation
 */

#define MASK_ON(type, start, len)     ((type)(~(((type)~0) << len)) << start)
#define MASK_OFF(type, n, start, len) ((type)~MASK_ON(start, len))
#define FILP_BITS(type, start, len)   (n ^ MASK_ON(start, len))
#define GET_BIT(n, i)                 ((n >> i) & 1)


/**
 * Prints out each bit in an `unsigned short`
 * @param n the number whose bits are to be printed
 */

void put_bits(unsigned short n){
    for (int i = 15; i >= 0; i--) {
        printf("%d", GET_BIT(n, i));
        if (i == 5 || i == 11) printf(" ");
    }
    printf("\n");
}

/**
 * Reverses the bits in an `unsigned short` and returns a copy
 * @param b the bit pattern
 * @return b with its bits reversed
 */

unsigned short rev_bits(unsigned short b) {
    unsigned short r = 0;
    for (int i = 0; i < 15; i++) {
        r <<= 1;
        r |= GET_BIT(b, i);
    }
    r <<= 1;
    return r;
}
```
