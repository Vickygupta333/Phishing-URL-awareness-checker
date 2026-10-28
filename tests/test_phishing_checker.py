import unittest

from phishing_checker import has_warnings, inspect_url


class InspectUrlTests(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(inspect_url(""), ["No URL entered."])

    def test_safe_sample_is_cautious_not_a_verdict(self):
        findings = inspect_url("https://www.example.com/login")
        self.assertEqual(
            findings,
            ["No listed warning signs found. This does NOT prove safety."],
        )
        self.assertFalse(has_warnings(findings))

    def test_ip_address_and_http_are_reported(self):
        findings = inspect_url("http://192.0.2.10/account")
        self.assertIn("Uses an IP address instead of a familiar domain.", findings)
        self.assertIn("Uses HTTP. HTTPS alone does not prove trust.", findings)
        self.assertTrue(has_warnings(findings))

    def test_at_symbol_and_http_are_reported(self):
        findings = inspect_url("http://example.com@sample.invalid/login")
        self.assertIn("Contains an @ symbol; inspect carefully.", findings)
        self.assertIn("Uses HTTP. HTTPS alone does not prove trust.", findings)

    def test_hostname_and_punycode_warnings(self):
        many_segments = inspect_url("https://a.b.c.d.e.example.invalid/path")
        punycode = inspect_url("https://xn--example.invalid/")
        self.assertIn("Contains many hostname segments/subdomains.", many_segments)
        self.assertIn("Contains a punycode-style hostname.", punycode)

    def test_long_url_is_reported(self):
        findings = inspect_url("https://example.com/" + ("a" * 100))
        self.assertIn("Unusually long URL (over 100 characters).", findings)

    def test_malformed_input_is_reported_without_raising(self):
        self.assertEqual(
            inspect_url("https://[not-an-ip"),
            ["This text is not a valid URL format."],
        )
        self.assertEqual(
            inspect_url("https://example.com:invalid"),
            ["This text is not a valid URL format."],
        )
        self.assertEqual(
            inspect_url("not a url"),
            ["This text is not a valid URL format."],
        )

    def test_empty_findings_are_not_warnings(self):
        self.assertFalse(has_warnings([]))


if __name__ == "__main__":
    unittest.main()
