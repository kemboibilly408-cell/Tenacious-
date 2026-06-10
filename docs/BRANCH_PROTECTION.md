# Branch Protection Rules Setup Guide

This guide will help you configure branch protection rules for the `main` branch of your repository.

## 🔒 Why Branch Protection?

Branch protection ensures that:
- ✅ All code changes go through pull requests
- ✅ Code reviews happen before merging
- ✅ Automated tests pass before merge
- ✅ Code quality standards are maintained
- ✅ Commit history stays clean

## 🛠️ Step-by-Step Setup

### Step 1: Navigate to Branch Protection Settings

1. Go to your repository: [Tenacious-](https://github.com/kemboibilly408-cell/Tenacious-)
2. Click **Settings** (top right)
3. Click **Branches** in the left sidebar
4. Click **Add rule** button

### Step 2: Configure the Rule

#### Branch name pattern
```
main
```

### Step 3: Enable Protection Options

#### ✅ Require a pull request before merging
- Check this box
- **Require approvals:** 1 (or more for teams)
- **Dismiss stale pull request approvals when new commits are pushed:** Check
- **Require review from code owners:** Check

#### ✅ Require status checks to pass before merging
- Check this box
- **Require branches to be up to date before merging:** Check
- **Status checks that must pass before merging:**
  - `test (3.8)`
  - `test (3.9)`
  - `test (3.10)`
  - `test (3.11)`
  - `code-quality`
  - `build` (Docker workflow)

#### ✅ Require code reviews (Optional but recommended)
- **Require approvals:** 1
- **Dismiss stale pull request approvals:** Check

#### ✅ Restrict who can push to matching branches
- **Restrict who can push to matching branches:** Check
- Add yourself: `@kemboibilly408-cell`

#### ⭐ Additional Recommended Settings
- **Require signed commits:** Check (for security)
- **Include administrators:** Check (applies rules to admins too)

### Step 4: Save

Click the **Create** button at the bottom to save your branch protection rule.

## 📋 What Gets Protected

After setup, here's what's protected:

| Protection | Enforced |
|-----------|----------|
| Direct commits to `main` | ❌ Not allowed |
| Pull requests required | ✅ Yes |
| Approvals required | ✅ Yes (1) |
| Tests must pass | ✅ Yes |
| Code review required | ✅ Yes |
| Up-to-date with main | ✅ Yes |

## 🚀 Workflow After Protection is Enabled

### Creating Features

```bash
# Create feature branch
git checkout -b feature/my-feature

# Make changes
git add .
git commit -m "Add feature"

# Push to GitHub
git push origin feature/my-feature
```

### Creating Pull Request

1. Go to GitHub repo
2. Click **New Pull Request**
3. Select your feature branch
4. Add description following the template
5. Assign reviewers (automatically assigned via CODEOWNERS)
6. Wait for automated checks to pass
7. Request review
8. Once approved and all checks pass, click **Merge**

## 🔄 Branches You Might Need

Consider protecting these branches too:

```
main       - Protected (production-ready)
develop    - Protected (staging/development)
hotfix/*   - Optional protection for hotfix branches
```

## ✅ Verification

To verify branch protection is working:

1. Try to push directly to `main`:
   ```bash
   git push origin main  # This should fail
   ```

2. Create a PR and notice:
   - Automated reviewers assigned
   - Status checks run automatically
   - Merge button disabled until all checks pass

## 📚 Additional Resources

- [GitHub Branch Protection Docs](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)
- [CODEOWNERS Reference](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)

---

**Remember:** Branch protection helps maintain code quality and prevents accidental merges to production! 🎯
