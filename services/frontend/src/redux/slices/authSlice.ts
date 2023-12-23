import { createSlice } from '@reduxjs/toolkit';
// Define a type for the slice state
type authState = { value: boolean }

// Define the initial state using that type
const initialState: authState = { value: false }

export const authSlice = createSlice({
  name: 'auth', initialState,
  reducers: { switchState: (state) => { state.value = !state.value }, },
})

export const { switchState } = authSlice.actions

export default authSlice.reducer