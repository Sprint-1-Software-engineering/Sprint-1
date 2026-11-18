
const loginForm = document.getElementById("loginForm");
const registerForm = document.getElementById("registerForm");
const API_BASE_URL = window.location.protocol === "http:"
  && window.location.hostname === "127.0.0.1"
  && window.location.port === "8000"
  ? ""
  : "http://127.0.0.1:8000";

function setupPasswordToggle(toggleId, inputId) {
  const toggle = document.getElementById(toggleId);
  const input = document.getElementById(inputId);
  if (!toggle || !input) return;

  toggle.addEventListener("click", () => {
    const isVisible = input.type === "text";
    input.type = isVisible ? "password" : "text";
    toggle.classList.toggle("visible", !isVisible);
    toggle.setAttribute("aria-label", isVisible ? "Şifreyi göster" : "Şifreyi gizle");
  });
}

setupPasswordToggle("passwordToggle", "password");
setupPasswordToggle("registerPasswordToggle", "registerPassword");

function setError(input, messageElement, message) {
  messageElement.textContent = message;
  input.closest(".input-wrap").classList.toggle("invalid", Boolean(message));
  input.setAttribute("aria-invalid", Boolean(message));
}

if (loginForm) {
  const emailInput = document.getElementById("email");
  const passwordInput = document.getElementById("password");

  loginForm.addEventListener("submit", (event) => {
    event.preventDefault();

    const emailError = document.getElementById("emailError");
    const passwordError = document.getElementById("passwordError");
    const email = emailInput.value.trim();
    const password = passwordInput.value;

    let isValid = true;

    if (!email) {
      setError(emailInput, emailError, "E-posta adresinizi girin.");
      isValid = false;
    } else if (!emailInput.checkValidity()) {
      setError(emailInput, emailError, "Geçerli bir e-posta adresi girin.");
      isValid = false;
    } else {
      setError(emailInput, emailError, "");
    }

    if (!password) {
      setError(passwordInput, passwordError, "Şifrenizi girin.");
      isValid = false;
    } else if (password.length < 6) {
      setError(passwordInput, passwordError, "Şifre en az 6 karakter olmalıdır.");
      isValid = false;
    } else {
      setError(passwordInput, passwordError, "");
    }

    if (isValid) {
      const submitButton = loginForm.querySelector(".submit-button");
      submitButton.querySelector("span").textContent = "Giriş yapılıyor...";
      submitButton.disabled = true;

      fetch(`${API_BASE_URL}/api/v1/auth/login`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password })
      })
        .then(async (response) => {
          const data = await response.json();
          if (!response.ok) throw new Error(data.message || "Giriş yapılamadı.");
          localStorage.setItem("tutorbridge_access_token", data.accessToken);
          submitButton.querySelector("span").textContent = "Yönlendiriliyorsunuz...";
          window.location.href = "main_page.html";
        })
        .catch((error) => {
          submitButton.disabled = false;
          submitButton.querySelector("span").textContent = "Giriş yap";
          document.getElementById("passwordError").textContent = error.message;
        });
    }
  });

  [emailInput, passwordInput].forEach((input) => {
    input.addEventListener("input", () => {
      const messageElement = input === emailInput
        ? document.getElementById("emailError")
        : document.getElementById("passwordError");
      setError(input, messageElement, "");
    });
  });
}

if (registerForm) {
  registerForm.addEventListener("submit", (event) => {
    event.preventDefault();

    let isValid = true;
    const requiredTextFields = [
      ["firstName", "firstNameError", "Adınızı girin."],
      ["lastName", "lastNameError", "Soyadınızı girin."],
      ["registerEmail", "registerEmailError", "E-posta adresinizi girin."]
    ];

    requiredTextFields.forEach(([inputId, errorId, emptyMessage]) => {
      const input = document.getElementById(inputId);
      const error = document.getElementById(errorId);
      if (!input.value.trim()) {
        setError(input, error, emptyMessage);
        isValid = false;
      } else if (input.type === "email" && !input.checkValidity()) {
        setError(input, error, "Geçerli bir e-posta adresi girin.");
        isValid = false;
      } else {
        setError(input, error, "");
      }
    });

    const role = registerForm.querySelector('input[name="role"]:checked');
    const roleError = document.getElementById("roleError");
    roleError.textContent = role ? "" : "Hesap türünüzü seçin.";
    if (!role) isValid = false;

    const password = document.getElementById("registerPassword");
    const confirmPassword = document.getElementById("confirmPassword");
    const passwordError = document.getElementById("registerPasswordError");
    const confirmError = document.getElementById("confirmPasswordError");

    if (!password.value) {
      setError(password, passwordError, "Şifrenizi girin.");
      isValid = false;
    } else if (password.value.length < 12) {
      setError(password, passwordError, "Şifre en az 12 karakter olmalıdır.");
      isValid = false;
    } else {
      setError(password, passwordError, "");
    }

    if (!confirmPassword.value) {
      setError(confirmPassword, confirmError, "Şifrenizi tekrar girin.");
      isValid = false;
    } else if (confirmPassword.value !== password.value) {
      setError(confirmPassword, confirmError, "Şifreler eşleşmiyor.");
      isValid = false;
    } else {
      setError(confirmPassword, confirmError, "");
    }

    const terms = document.getElementById("terms");
    const termsError = document.getElementById("termsError");
    termsError.textContent = terms.checked ? "" : "Devam etmek için koşulları kabul edin.";
    if (!terms.checked) isValid = false;

    if (isValid) {
      const submitButton = registerForm.querySelector(".submit-button");
      submitButton.querySelector("span").textContent = "Hesap oluşturuluyor...";
      submitButton.disabled = true;

      const firstName = document.getElementById("firstName").value.trim();
      const lastName = document.getElementById("lastName").value.trim();

      fetch(`${API_BASE_URL}/api/v1/auth/register`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          name: `${firstName} ${lastName}`,
          email: document.getElementById("registerEmail").value.trim(),
          password: password.value,
          role: registerForm.querySelector('input[name="role"]:checked').value
        })
      })
        .then(async (response) => {
          const data = await response.json();
          if (!response.ok) throw new Error(data.message || "Kayıt oluşturulamadı.");
          submitButton.querySelector("span").textContent = "Hesap oluşturuldu";
          setTimeout(() => window.location.href = "login.html", 700);
        })
        .catch((error) => {
          submitButton.disabled = false;
          submitButton.querySelector("span").textContent = "Hesap oluştur";
          document.getElementById("registerEmailError").textContent = error.message;
        });
    }
  });

  registerForm.querySelectorAll("input").forEach((input) => {
    input.addEventListener("input", () => {
      const errorId = input.id ? `${input.id}Error` : "";
      const error = errorId ? document.getElementById(errorId) : null;
      if (error) setError(input, error, "");
    });
  });

  registerForm.querySelectorAll('input[name="role"]').forEach((input) => {
    input.addEventListener("change", () => {
      document.getElementById("roleError").textContent = "";
    });
  });

  document.getElementById("terms").addEventListener("change", () => {
    document.getElementById("termsError").textContent = "";
  });
}

const menuToggle = document.getElementById("menuToggle");
const obsSidebar = document.getElementById("obsSidebar");
const sidebarBackdrop = document.getElementById("sidebarBackdrop");

if (menuToggle && obsSidebar && sidebarBackdrop) {
  const setSidebarOpen = (isOpen) => {
    obsSidebar.classList.toggle("open", isOpen);
    sidebarBackdrop.classList.toggle("visible", isOpen);
    menuToggle.setAttribute("aria-expanded", String(isOpen));
    menuToggle.setAttribute("aria-label", isOpen ? "Menüyü kapat" : "Menüyü aç");
  };

  menuToggle.addEventListener("click", () => {
    setSidebarOpen(!obsSidebar.classList.contains("open"));
  });
  sidebarBackdrop.addEventListener("click", () => setSidebarOpen(false));
  obsSidebar.querySelectorAll(".obs-nav-link").forEach((link) => {
    link.addEventListener("click", () => setSidebarOpen(false));
  });
}

const logoutButton = document.getElementById("logoutButton");
if (logoutButton) {
  logoutButton.addEventListener("click", () => {
    localStorage.removeItem("tutorbridge_access_token");
    window.location.href = "login.html";
  });
}

const userNameTargets = document.querySelectorAll("[data-user-name]");
if (userNameTargets.length > 0) {
  const setUserName = (name) => {
    userNameTargets.forEach((element) => {
      element.textContent = name;
    });
    const initial = Array.from(name.trim())[0] || "Ö";
    document.querySelectorAll("[data-user-initial]").forEach((element) => {
      element.textContent = initial.toLocaleUpperCase("tr-TR");
    });
  };

  const accessToken = localStorage.getItem("tutorbridge_access_token");
  if (accessToken) {
    fetch(`${API_BASE_URL}/api/v1/users/me`, {
      headers: { Authorization: `Bearer ${accessToken}` }
    })
      .then(async (response) => {
        const data = await response.json();
        if (response.status === 401) {
          localStorage.removeItem("tutorbridge_access_token");
          window.location.href = "login.html";
          return;
        }
        if (!response.ok) throw new Error(data.message || "Kullanıcı bilgisi alınamadı.");
        setUserName(data.name);
      })
      .catch((error) => {
        const nameError = document.getElementById("userNameError");
        if (nameError) nameError.textContent = error.message;
      });
  }
}
