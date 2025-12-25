from playwright.sync_api import sync_playwright

def verify_x_crop():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Test Home Page
        print("Navigating to home page...")
        page.goto("http://127.0.0.1:5000/")
        page.wait_for_selector(".logo")

        # Check title
        title = page.title()
        assert "X-Crop" in title, f"Title should contain 'X-Crop', got '{title}'"

        page.screenshot(path="verification/home_page_xcrop.png")
        print("Home page screenshot saved.")

        # Test Search Results
        print("Performing search...")
        page.fill('input[name="q"]', 'Python')
        # Click the submit button
        page.click('button[type="submit"]')
        page.wait_for_selector(".ai-overview")

        # Check results title
        title = page.title()
        assert "X-Crop" in title, f"Title should contain 'X-Crop', got '{title}'"

        page.screenshot(path="verification/results_page_xcrop.png")
        print("Results page screenshot saved.")

        browser.close()

if __name__ == "__main__":
    verify_x_crop()
