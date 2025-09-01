diff --git a//dev/null b/company_evaluator.py
index 0000000000000000000000000000000000000000..3d45e4845064bb4c3613bef879b69152df9f9dcd 100644
--- a//dev/null
+++ b/company_evaluator.py
@@ -0,0 +1,63 @@
+"""Simple stock evaluator for educational purposes. Not financial advice."""
+import sys
+from typing import Optional, Any
+
+try:
+    import yfinance as yf
+except Exception:  # pragma: no cover - library may not be available during tests
+    yf = None  # type: ignore
+
+
+def fetch_company_info(ticker: str) -> Optional[Any]:
+    """Return a yfinance Ticker object or None on failure."""
+    if yf is None:
+        print("yfinance library is not installed.", file=sys.stderr)
+        return None
+    try:
+        return yf.Ticker(ticker)
+    except Exception as exc:  # pragma: no cover - network issues
+        print(f"Failed to retrieve data: {exc}", file=sys.stderr)
+        return None
+
+
+def evaluate_company(ticker: str) -> Optional[str]:
+    ticker_obj = fetch_company_info(ticker)
+    if ticker_obj is None:
+        return None
+    try:
+        history = ticker_obj.history(period="1y")
+    except Exception as exc:  # pragma: no cover - network issues
+        print(f"Failed to download history: {exc}", file=sys.stderr)
+        return None
+    if history.empty:
+        print("No historical data available.", file=sys.stderr)
+        return None
+    current_price = history["Close"].iloc[-1]
+    avg_price = history["Close"].mean()
+    if current_price > avg_price:
+        return (
+            f"{ticker} is trading above its yearly average. This could indicate positive momentum,\n"
+            "but always conduct thorough research before investing."
+        )
+    else:
+        return (
+            f"{ticker} is trading below its yearly average. This might signal caution,\n"
+            "and additional investigation is recommended."
+        )
+
+
+def main() -> None:
+    print("Enter the ticker symbol of the company (e.g., AAPL for Apple):")
+    ticker = input().strip().upper()
+    if not ticker:
+        print("No ticker provided.")
+        return
+    result = evaluate_company(ticker)
+    if result:
+        print(result)
+    else:
+        print("Unable to evaluate the company.")
+
+
+if __name__ == "__main__":
+    main()
