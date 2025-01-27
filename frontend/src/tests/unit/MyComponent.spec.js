import { mount } from "@vue/test-utils";
import MyComponent from "@/components/HelloWorld.vue";

describe("HelloWorld", () => {
  it("emits an event when clicked", () => {
    const wrapper = mount(MyComponent);
    wrapper.find("button").trigger("click");
    expect(wrapper.emitted("click")).toBeTruthy();
  });
});