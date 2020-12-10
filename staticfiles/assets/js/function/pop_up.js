const customModal = document.querySelector('.custom-modal');

// Click listener for activation
const modalButton = document.querySelector('.modalActivate');
modalButton.addEventListener('click', activateModal);

// Click listener for deactivation
const closeButton = document.querySelector('.custom-modal-close');
closeButton.addEventListener('click', deactivateModal);

function activateModal() {
  customModal.style.display = 'block';
}

function deactivateModal() {
  customModal.style.display = 'none';
}
