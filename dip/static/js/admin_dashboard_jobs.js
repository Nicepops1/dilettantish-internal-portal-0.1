const deleteButtons = document.querySelectorAll('.job-titles-list__button--delete');

const jobTitleEditable = document.querySelectorAll('.job-titles-list__name');


deleteButtons.forEach(button => {
  button.addEventListener('click', (e) => {

    e.preventDefault()

    const jobTitleId = button.parentNode.id;

    deleteJobTitle(jobTitleId);
    
  });
});

jobTitleEditable.forEach(field => {

  const oldJobTitle = field.textContent;

  field.addEventListener('keypress', (e) => {

    const jobTitleId = field.parentNode.id;

    if (e.key === 'Enter') {
      e.preventDefault();
      newJobTitle = field.textContent;
      updateJobTitle(jobTitleId, newJobTitle, oldJobTitle);
    }
  })
})


function deleteJobTitle(jobTitleId) {
  fetch(`/admin/dashboard/job-titles/${jobTitleId}/delete`)
  .then((response) => {
    if (response.ok) {
      const el = document.querySelector(`.job-titles-list__item[id="${ jobTitleId }"]`);
      el.remove();
    }
  })
}

function updateJobTitle(jobTitleId, newJobTitle) {

  fetch(`/admin/dashboard/job-titles/${jobTitleId}/update`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      id: jobTitleId,
      title: newJobTitle
    })
  })
  .then((response) => {
    if (response.ok) {
      const el = document.querySelector(`.job-titles-list__item[id="${ jobTitleId }"] > .job-titles-list__name`);
      el.blur()
    } else {
      response.text().then((error) => {
        showError(error)
      })
    }
  })
}


var timer = null;

function showError(message) {
  if (timer !== null) {
      clearTimeout(timer);
      timer = null;
  }
  var errorElement = document.querySelector(".job-titles-list__temp-message-error");
  errorElement.innerHTML = message;
  errorElement.style.display = 'block';
  timer = setTimeout(function(){ errorElement.style.display = 'none'; }, 2000);
}