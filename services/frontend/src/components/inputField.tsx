/* eslint-disable @next/next/no-img-element */

export default function InputField({ id, type, label, placeholder, className }: { id?: string, type: string, label?: string, placeholder?: string, className?: string }) {
    return (
        <div className={`flex flex-col ${className}`}>
            {label
                ? <label htmlFor={id}>{label} <b className="text-red-600">*</b></label>
                : undefined
            }
            <input
                id={id} type={type} placeholder={placeholder} required
                className="mt-[4px] border-2 rounded-[8px] px-[12px] py-[8px]"
            />
        </div>
    )
}
