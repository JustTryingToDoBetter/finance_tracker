import { mount } from "@vue/test-utils";
import ExpenseForm from "@/components/ExpenseForm.vue";
import axios from "@/services/axios";

// Mock axios
jest.mock("@/services/axios");

describe("ExpenseForm", () => {
  let wrapper;

  beforeEach(() => {
    wrapper = mount(ExpenseForm);
  });

  afterEach(() => {
    jest.clearAllMocks();
  });

  it("submits the form and emits an event when valid data is entered", async () => {
    // Mock the axios post request
    axios.post.mockResolvedValue({});

    // Fill out the form
    await wrapper.find("#amount").setValue(100);
    await wrapper.find("#category").setValue("Food");
    await wrapper.find("#date").setValue("2023-10-01");
    await wrapper.find("#description").setValue("Lunch");

    // Submit the form
    await wrapper.find("form").trigger("submit.prevent");

    // Ensure the form is submitting
    expect(wrapper.vm.isSubmitting).toBe(true);

    // Wait for the axios request to complete
    await wrapper.vm.$nextTick();

    // Ensure the form is reset
    expect(wrapper.vm.form).toEqual({
      amount: "",
      category: "",
      date: "",
      description: "",
    });

    // Ensure the success message is displayed
    expect(wrapper.vm.successMessage).toBe("Expense added successfully!");

    // Ensure the expense-added event is emitted
    expect(wrapper.emitted("expense-added")).toBeTruthy();

    // Ensure the submit button is no longer disabled
    expect(wrapper.find("button").attributes("disabled")).toBeUndefined();
  });

  it("displays an error message when required fields are missing", async () => {
    // Submit the form without filling it out
    await wrapper.find("form").trigger("submit.prevent");

    // Ensure the error message is displayed
    expect(wrapper.vm.errorMessage).toBe("Failed to add expense. Please try again.");

    // Ensure the form is not reset
    expect(wrapper.vm.form).toEqual({
      amount: "",
      category: "",
      date: "",
      description: "",
    });

    // Ensure the submit button is not disabled
    expect(wrapper.find("button").attributes("disabled")).toBeUndefined();
  });

  it("disables the submit button while submitting", async () => {
    // Mock the axios post request
    axios.post.mockResolvedValue({});

    // Fill out the form
    await wrapper.find("#amount").setValue(100);
    await wrapper.find("#category").setValue("Food");
    await wrapper.find("#date").setValue("2023-10-01");
    await wrapper.find("#description").setValue("Lunch");

    // Submit the form
    await wrapper.find("form").trigger("submit.prevent");

    // Ensure the submit button is disabled
    expect(wrapper.find("button").attributes("disabled")).toBeDefined();

    // Wait for the axios request to complete
    await wrapper.vm.$nextTick();

    // Ensure the submit button is no longer disabled
    expect(wrapper.find("button").attributes("disabled")).toBeUndefined();
  });

  it("resets the form after a successful submission", async () => {
    // Mock the axios post request
    axios.post.mockResolvedValue({});

    // Fill out the form
    await wrapper.find("#amount").setValue(100);
    await wrapper.find("#category").setValue("Food");
    await wrapper.find("#date").setValue("2023-10-01");
    await wrapper.find("#description").setValue("Lunch");

    // Submit the form
    await wrapper.find("form").trigger("submit.prevent");

    // Wait for the axios request to complete
    await wrapper.vm.$nextTick();

    // Ensure the form is reset
    expect(wrapper.vm.form).toEqual({
      amount: "",
      category: "",
      date: "",
      description: "",
    });
  });
});