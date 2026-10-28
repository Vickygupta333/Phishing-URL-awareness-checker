# Test Results

Python version used: 3.13.5  |  Operating system: Windows  |  Date: 2026-10-28

The program was run with each sample below. Actual results are summarized from its printed output.

| # | Input | Expected result | Actual result | Pass/Fail |
|---|-------|-----------------|---------------|-----------|
| 1 | `https://www.example.com/login` | No listed warning signs; not a safety guarantee | No listed warning signs found. This does NOT prove safety. | PASS |
| 2 | `http://192.0.2.10/account` | IP address + HTTP | IP address and HTTP warnings; review summary showed 2 signs. | PASS |
| 3 | `http://example.com@sample.invalid/login` | `@` symbol + HTTP | `@` symbol and HTTP warnings; review summary showed 2 signs. | PASS |
| 4 | `https://a.b.c.d.e.example.invalid/path` | Many hostname segments | Many hostname segments warning; review summary showed 1 sign. | PASS |
| 5 | `https://xn--example.invalid/` | Punycode-style hostname | Punycode-style hostname warning; review summary showed 1 sign. | PASS |

## Notes

The five workbook samples produced their expected warning messages. The empty-input and malformed-input examples also returned readable messages, and `q` exited the program cleanly.
