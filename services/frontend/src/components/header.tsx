/* eslint-disable @next/next/no-img-element */
"use client";

import { switchState } from "@/redux/slices/authSlice";
import { RootState } from "@/redux/store";
import Link from "next/link";
import { useDispatch, useSelector } from "react-redux";
import SignInForm from "@/components/signIn";
import axios from "axios";

axios.defaults.baseURL = "https://compas.fun/api/v1/"

export default function Header() {

    const dispatch = useDispatch();
    const auth = useSelector((state: RootState) => state.auth.value);

    return (
        <header className="flex justify-between h-[12vh] items-center">
            <Link href="/">
                <img
                    src="/icons/logo.png" alt="Logo"
                    className="h-[8vh] select-none"
                />
            </Link>
            <nav className="w-[60%] flex justify-between font-bold text-[1.4em]">
                <Link href="/rorschach">Тест Роршаха</Link>
                <Link href="/guidance">Профориентация</Link>
                <Link href="/professions">Список профессий</Link>
                <Link href="/youtube">Привязка YouTube</Link>
            </nav>
            <button className={`
                bg-[#051531] text-white px-[36px] 
                py-[12px] rounded-[12px] tracking-wider
                text-xl font-bold
            `} onClick={() => dispatch(switchState())}>Авторизация</button>
            {auth ? <SignInForm /> : undefined}
        </header>
    )
}
