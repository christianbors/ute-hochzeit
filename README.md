# Wedding guest information page

A small, responsive static wedding website for GitHub Pages. Fonts and colors are controlled through CSS variables, and the site makes no external font requests by default.

## Project structure

```text
wedding-guest-page/
├── .github/
│   └── workflows/
│       └── deploy-pages.yml  # Automatic GitHub Pages deployment
├── assets/
│   ├── css/styles.css        # Theme variables and layout
│   ├── js/main.js            # Optional enhancements
│   └── images/favicon.svg
├── .nojekyll                 # Serve the files as-is
├── index.html
├── robots.txt
└── README.md
```

## Customize the content

Edit `index.html` and replace all example names, dates, addresses, contacts, hotel links, and map links.

## Change fonts and colors

Edit the variables at the top of `assets/css/styles.css`:

```css
:root {
  --font-heading: Georgia, "Times New Roman", serif;
  --font-body: Inter, ui-sans-serif, system-ui, sans-serif;
  --color-background: #fffdf9;
  --color-tinted: #f5efe8;
  --color-text: #302c29;
  --color-primary: #765645;
  --color-accent: #b58b72;
}
```

The default uses system fonts. To use custom fonts, add WOFF2 files under `assets/fonts/`, declare them using `@font-face`, and update `--font-heading` or `--font-body`.

## Preview locally

```bash
python3 -m http.server 8080
```

Open `http://localhost:8080`.

## Publish with GitHub Pages

1. Create a GitHub repository and push this folder to its `main` branch.
2. Open **Settings → Pages** in the repository.
3. Under **Build and deployment**, select **GitHub Actions** as the source.
4. Open the **Actions** tab and wait for the deployment workflow to finish.
5. The site will be available at `https://YOUR-USERNAME.github.io/REPOSITORY-NAME/`.

Typical first push:

```bash
git init
git add .
git commit -m "Create wedding guest page"
git branch -M main
git remote add origin git@github.com:YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```

All asset paths are relative, so the page works both at a project URL and on a custom domain.

## Custom domain

Add your domain in **Settings → Pages → Custom domain**, then configure the DNS records requested by GitHub. Generate the QR code only after the final URL is established.

## Repository and site privacy

- GitHub Free supports Pages from public repositories.
- GitHub Pro, Team, and Enterprise plans can publish Pages from private repositories.
- A private repository does **not** by itself password-protect the published website.
- GitHub's privately published Pages sites are intended for eligible organization/enterprise access. Visitors need GitHub accounts and repository read access, which is usually unsuitable for wedding guests.
- GitHub Pages cannot implement server-side HTTP Basic Authentication or a shared guest password because it only serves static files.

A JavaScript password prompt would only hide the page cosmetically: its password and protected content remain downloadable in the browser. Do not use it for information that truly needs access control.

For a public wedding logistics page, keep the existing `noindex` metadata and `robots.txt`, use a non-obvious URL, and avoid highly sensitive personal information. These measures reduce discovery but are not authentication.
